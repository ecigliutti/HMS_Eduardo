from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView, View
from .models import Room, Booking
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability


# Create your views here.

#Original view function
#class RoomList(ListView):
#    model = Room
class RoomListView(ListView):
    model = Room

class BookingList(ListView):
    model = Booking

class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)

        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)            
            context={
                'room_category': room_category,
                'form' : form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('category does not exist')
        
    dayin = ()
    dayout = ()
    apt = ()

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)
        datadayin = (form.data['check_in'])
        datadayout = (form.data['check_out']) 
        category = category  
        mytest = (form.is_valid()) 
        return HttpResponse(form) 

        if request.method == 'POST':
            #return HttpResponse(mytest)
            #return HttpResponse(dayin + dayout)
            #return HttpResponse('form is valid')
            #if form.is_valid():
            if mytest == False:
                #return HttpResponse('form is valid')
            #else:
                #return HttpResponse('form NOT valid')
                data = form.cleaned_data
                return HttpResponse(data)                               
                

                available_rooms=[]

                for room in room_list:
                    
                    if check_availability(room, data['check_in'], data['check_out']):
                        available_rooms.append(room)                

                if len(available_rooms) > 0:
                    room = available_rooms[0]
                    booking = Booking.objects.create(
                        user=self.request.user,
                        room=room,
                        check_in=data['check_in'],
                        check_out=data['check_out']                
                )  
                
                    booking.save()
        else:
            return HttpResponse('This Apartment is not available')



class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],
        )  
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This Apartment is not available')