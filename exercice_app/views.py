from django.shortcuts import render,redirect
from login_app.models import User
from django.contrib import messages
from.models import Trip

def index(request):
    context={
        "trips":Trip.objects.filter(user = User.objects.get(id = request.session['id']))
    }
    return render(request,"exam.html",context)
def new_trip(request):
    return render(request,"new_trip.html")

def create_trip(request):
    errors=Trip.objects.validator(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect("/exam/trips/new")
    else:
        Trip.objects.create(
            destination=request.POST["destination"],
            start_date=request.POST["start_date"],
            end_date=request.POST["end_date"],
            plan=request.POST["plan"],
            user=User.objects.get(id=request.session["id"])
        )
        return redirect("/exam")

def remove_trip(request,trip_id):
    Trip.objects.get(id=trip_id).delete()
    return redirect("/exam/")



def edit_trip(request,trip_id):
    context={
            "trips":Trip.objects.get(id=trip_id)
    }
    return render(request,"edit_trip.html",context)

def update_trip(request,trip_id):
    errors=Trip.objects.validator(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect(f"/exam/trips/{trip_id}/edit")
    else:
        # isn't actually targeting properties of the trip
        trips=Trip.objects.get(id=trip_id)
        trips.destination=request.POST["destination"]
        trips.start_date=request.POST["start_date"]
        trips.end_date=request.POST["end_date"]
        trips.plan=request.POST["plan"]
        trips.save()
    
    return redirect("/exam")

def view_detail(request,trip_id):
    context={
        "trips":Trip.objects.get(id=trip_id)
        
    }
    return render(request,"detail_user.html",context)





