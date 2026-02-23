from django.shortcuts import render,redirect
from .models import HotelRoom
from .forms import HotelRoomForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign_in')
def bookHotel(request):
    form = HotelRoomForm()
    if(request.method == 'POST'):
        form = HotelRoomForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('show_bookings')
        else:
            return HttpResponse("Something Went Wrong While Booking Hotel")
    template_name = 'management/book_hotel.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='sign_in')
def showBookings(request):
    objs = HotelRoom.objects.all()
    template_name = 'management/show_bookings.html'
    context = {'records':objs}
    return render(request,template_name,context)

def updateBookings(request,pk):
    obj = HotelRoom.objects.get(id=pk)
    form = HotelRoomForm(instance=obj)
    if(request.method == 'POST'):
        form = HotelRoomForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('show_bookings')
        else:
            return HttpResponse("Something Went Wrong While Updating Hotel Room")
    template_name = 'management/update_bookings.html'
    context = {'form':form}
    return render(request,template_name,context)

def deleteBookings(request,pk):
    obj = HotelRoom.objects.get(id=pk)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('show_bookings')
    template_name = 'management/delete_bookings.html'
    context = {'obj':obj}
    return render(request,template_name,context)