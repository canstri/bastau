from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from accounts.models import Profile
from .solve_problem_form import CheckProblemForm

from .expression_form import ExpressionForm
from .theorem_form import TheoremForm
from .models import Problem, CheckProblem, Lemma, Theorem

from olymps.models import Olymp, RatingOlymp
from hashtags.models import Hashtag
from maths.lemmas import LemmaCode
from maths.theorems import TheoremCode
from news.views import create_action

def create_problem(request, input_form):
    form = input_form
    text = ''
    if form.is_valid():
        
        new_problem, created1 = Problem.objects.get_or_create(
                            user = request.user,
                            content_type= ContentType.objects.get(model=form.cleaned_data.get("content_type")),
                            object_id = form.cleaned_data.get('object_id'),
                            content = form.cleaned_data.get("content"),
                            title = form.cleaned_data.get("title"),
                            level = form.cleaned_data.get("level"),
                        )
        new_problem.content2 = new_problem.content.replace("@", " ").replace("$", " ")
        new_problem.save()
        temp_hashtag = ''
        wright = False
        hashtag_array = []
        hashtag_string = ''
        hashtag_string = form.cleaned_data.get("hashtags")
        new_problem.hashtags = []
        print(form.cleaned_data.get("hashtags"), hashtag_string, new_problem.hashtags)
        hashtag_string += ' ,' 
        for i in range(0, len(hashtag_string)):
            if hashtag_string[i] == '#':
                wright = True
            if hashtag_string[i] == ' ':
                if temp_hashtag != '':
                    temp_hashtag = temp_hashtag[1:]
                    new_problem.hashtags.append(temp_hashtag)
                    its_ok = False
                    for hs in Hashtag.objects.all():
                        if hs.name == temp_hashtag:
                            new_problem.hashtag_list.add(hs)
                            its_ok = True
                    if its_ok == False:
                        new_problem.hashtag_list.create(name = temp_hashtag)
                #print("create_hash: ", new_problem.hashtags)
                temp_hashtag = ''
                wright = False
            if wright == True:
                temp_hashtag += hashtag_string[i]
        new_problem.save()

        for p in Profile.objects.all():
            check_problem, created2 = CheckProblem.objects.get_or_create(
                user = p.user.id,
                problem_id = new_problem.id,
                solved = False,
                current_string = '',
            )
            check_problem.actions = []
            counter1 = 0
            counter2 = 0
            temp_str1 = ''
            temp_str2 = ''
            for i in range(0, len(new_problem.content)):
                if new_problem.content[i] == '$':
                    counter1 += 1
                if counter1 % 2 == 1:    
                    temp_str1 += new_problem.content[i]
                if counter1 % 2 == 0 and counter1 > 0:
                    temp_str1 = temp_str1[1:]
                    check_problem.actions.append([temp_str1, 'Correct', 'given_in_task'])
                    temp_str1 = ''
                    counter1 = 0

                if new_problem.content[i] == '@':
                    counter2 += 1
                if counter2 % 2 == 1:    
                    temp_str2 += new_problem.content[i]
                if counter2 % 2 == 0 and counter2 > 0:
                    temp_str2 = temp_str2[1:]
                    check_problem.actions.append([temp_str2, 'Need to prove', 'given_in_task'])
                    temp_str2 = ''
                    counter2 = 0
            check_problem.save()

        olymp_any = Olymp.objects.all()[0]
        content_type_olymp = ContentType.objects.get_for_model(olymp_any.__class__)
        if new_problem.content_type == content_type_olymp:
            qset = RatingOlymp.objects.filter(olymp = new_problem.content_object)
            array_for_user = [new_problem.title, '0']
            for r in qset:
                r.points.append(array_for_user)
                r.save()
        return HttpResponseRedirect(new_problem.content_object.get_absolute_url())
    

def problem_delete(request, id):
    try:
        obj = Problem.objects.get(id=id)
    except:
        raise Http404

    if obj.user != request.user:
        reponse.status_code = 403
        return HttpResponse("You do not have permission to do this.")

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()

        for checkprblm in CheckProblem.objects.filter(problem_id = obj.id):
            checkprblm.delete()

        obj.delete()
        messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(parent_obj_url)
    
    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
    staff = "no"

    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"

    context = {
        "staff":staff,
        "profile":profile,
        "object": obj,
    }
    return render(request, "confirm_delete.html", context)

def problem_detail(request, id):
    try:
        obj = Problem.objects.get(id=id)
    except:
        raise Http404

    profile = 'admin'
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user.id)
    staff = "no"
    if request.user.is_staff or request.user.is_superuser:
        staff = "yes"

    #Checking expression inserted by user with basic lemmas
    content_object = obj.content_object 
    content_id = obj.content_object.id
    initial_data = {
            "content_type": obj.content_type,
            "object_id": obj.object_id
    }
    if request.user.id:
        check_problem = CheckProblem.objects.get(problem_id = obj.id, user = request.user.id)
    else:
        messages.warning(request, "You need to authanticate to see problems")
        return HttpResponseRedirect(obj.content_object.get_absolute_url())
    
    expression_form = ExpressionForm(request.POST or None)
    check_problem_form = CheckProblemForm(request.POST or None)
    theorem_form = TheoremForm(request.POST or None)
    expr1 = ''
    expr2 = ''
    action_check = ''

    if len(check_problem.actions) > 0:
        if check_problem.actions[0][1] == 'first_hidden':
            check_problem.actions.pop(0) 
            check_problem.save()
    if expression_form.is_valid():
        expr_id = expression_form.cleaned_data.get('exp_id')-1
        if 'delete' in request.POST:
            check_problem.actions.pop(expr_id) 
            check_problem.save()
            return HttpResponseRedirect(obj.get_absolute_url())
        if 'use' in request.POST:
            if check_problem.current_string != '':
                check_problem.current_string += '; '
                check_problem.save()
            check_problem.current_string = check_problem.current_string + check_problem.actions[expr_id][0] + " " + check_problem.actions[expr_id][1]
            check_problem.current_status = check_problem.actions[expr_id][1]
            check_problem.save()
            print(check_problem.current_string)
            return HttpResponseRedirect(obj.get_absolute_url())
        
    if check_problem_form.is_valid():
        if 'save' in request.POST:
            cstring = check_problem.current_string
            cstatus = check_problem.current_status
            if cstring == '':
                return HttpResponseRedirect(obj.get_absolute_url()) 
            found_old = False
            for actn in check_problem.actions:
                if cstring == actn[0]:
                    actn[1] = cstatus
                    found_old = True
                    break
            if found_old == False:
                check_problem.actions.append([cstring, cstatus, 'not_in_task'])
                print(cstring, cstatus, 'not_in_task')
            # check if problem is solved
            all_solved = True
            for actn in check_problem.actions:
                if actn[1] == 'Need to prove':
                    print("eboy", actn[0], '#', cstring, "#")
                    if actn[0] != cstring:
                        all_solved = False
                        print('False')
            #print('current_status', cstatus)
            # check if problem is fully solved
            if cstatus != "Correct":
                all_solved = False
            if all_solved == True:
                print('solved')
                if check_problem.solved == False: # if problem was not solved before
                    rating_olymp = RatingOlymp.objects.get(
                            user = profile,
                            olymp = content_object,
                        )
                    for prblm in rating_olymp.points:
                        if prblm[0] == obj.title:
                            prblm[1] = '7'
                    rating_olymp.points[0][1] = str(int(rating_olymp.points[0][1])+7)
                    rating_olymp.summary = rating_olymp.points[0][1]
                    rating_olymp.save()

                    for hashtag in obj.hashtags: 
                        hashtag = hashtag[1:]  # cross out "#" from hashtag name
                        number_theory_skill = 0
                        inequalities_skill = 0
                        for skill in profile.number_theory_skills: #search in number theory skills
                            if hashtag == skill[0]:  # if found needed skill of user
                                skill[1] = str(int(skill[1]) + obj.level) # increase this skill
                            number_theory_skill += int(skill[1])
                        for skill in profile.inequalities_skills: #search in inequality skills
                            if hashtag == skill[0]:  # if found needed skill of user
                                skill[1] = str(int(skill[1]) + obj.level) # increase this skill
                            inequalities_skill += int(skill[1])
                        profile.skills[0][1] = str(number_theory_skill/len(profile.number_theory_skills))
                        profile.skills[1][1] = str(inequalities_skill/len(profile.inequalities_skills))
                        rating = 0
                        for skill in profile.skills:
                            rating += float(skill[1])
                        profile.rating = rating
                        profile.save()
                        print('create_action in problem')
                    x=create_action(profile, obj)
                check_problem.solved = True
            check_problem.save()    

            check_problem.current_string = ''
            check_problem.current_status = ''
            check_problem.save()

            return HttpResponseRedirect(obj.get_absolute_url())  

        if 'clear' in request.POST:
            expr1 = ''
            action_check = ''
            check_problem.current_string = ''
            check_problem.current_status = ''
            check_problem.save()
            return HttpResponseRedirect(obj.get_absolute_url())  

        expr1 = check_problem_form.cleaned_data.get('expr1')
        
        if 'Replace variable' in request.POST:
            input_string = check_problem.current_string + '; ' + expr1
            result = getattr(TheoremCode, 'zamena')(input_string)
            if result[1] == '':
                return HttpResponseRedirect(obj.get_absolute_url()) 
            check_problem.current_string = result[0]
            check_problem.current_status = result[1]
            check_problem.save()
            return HttpResponseRedirect(obj.get_absolute_url())  

        if check_problem.current_string != '':
            expr2 = check_problem.current_string
        # preparing input string for lemmas
        input_string = ''
        if expr1 != '' and expr2 != '':
            input_string = expr2 + '; ' + expr1
        if expr1 != '' and expr2 == '':
            input_string = expr1

        #run lemmas
        for i in range (0, len(Lemma.objects.filter())):
            if action_check == "Correct":
                break            
            print("input_string", input_string)
            
            b = input_string.replace('√', 'sqrt')
            input_string = b
            print(input_string)
            action_check =  getattr(LemmaCode, Lemma.objects.filter()[i].name)(input_string) #Call all basic lemmas
        
        # update current expression and status
        check_problem.current_string = expr1
        check_problem.current_status = action_check
        check_problem.save()


    ht_array = []
    for hshtg in obj.hashtag_list.all():
        ht_array.append(hshtg)

    theorems = Theorem.objects.all()
    context = {
        "staff":staff,
        "profile":profile,
        "problem": obj,
        "check_problem_form": check_problem_form,
        "theorem_form": theorem_form,
        "check_problem": check_problem,
        "action_check":action_check,
        "expression_form": expression_form,
        "theorems":theorems,
        "current_string":check_problem.current_string,
        "current_status":check_problem.current_status,
        "ht_array":ht_array,
    }
    return render(request, "problem.html", context)



