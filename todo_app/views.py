from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ToDoItem, ToDoList, Cars

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context

class CarCreate(CreateView):
    model = Cars
    fields = [
        "title",
        "occupancy",
        "description",
    ]

    def get_initial(self):
        initial_data = super(CarCreate, self).get_initial()
        car_list = Cars.objects.get(id=self.kwargs["list_id"])
        initial_data["car"] = car_list
        return initial_data

    def get_context_data(self):
        context = super(CarCreate, self).get_context_data()
        car_list = Cars.objects.get(id=self.kwargs["list_id"])
        context["car_list"] = car_list
        context["title"] = "Create a new car"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.car_id])

class CarUpdate(UpdateView):
    model = Cars
    fields = [
        "title",
        "occupancy",
        "description"
    ]

    def get_context_data(self):
        context = super(CarUpdate, self).get_context_data()
        context["car_list"] = self.object.car_list
        context["title"] = "Edit car"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.car_list_id])

class CarsDelete(DeleteView):
    model = Cars
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class CarDelete(DeleteView):
    model = Cars

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["car_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = self.object.cars
        return context
class CarListView(ListView):
    model = ToDoList
    template_name = "todo_app/cars/index.html"