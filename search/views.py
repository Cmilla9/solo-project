from django.shortcuts import render
from django.db.models import Q
from food_truck_hub_app.models import BusinessUser

# def searchfood(request):
#     if request.method == 'POST':
#         query= request.GET.get('q')
#         print('in other app')
#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(food_category__icontains=query)

#             results= BusinessUser.objects.filter(lookups).distinct()

#             context={'results': results,
#                     'submitbutton': submitbutton}

#             return render(request, 'search.html', context)

#         else:
#             return render(request, 'search.html')

#     else:
#         return render(request, 'search.html')

def searchfood(request):
    print("in search app")
    if request.method == 'POST':
        query= request.POST.get('q')

        # submitbutton= request.GET.get('submit')
        # print(query)
        print("incorrect function")
        if query is not None:
            # lookups= Q(food_category__icontains=query)

            # results= BusinessUser.objects.filter(lookups).distinct()
            results= BusinessUser.objects.filter(food_category=query)
            # context={'results': results,
            #         'submitbutton': submitbutton}
            context={'results': results
                    }
            return render(request,'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
# Create your views here.
