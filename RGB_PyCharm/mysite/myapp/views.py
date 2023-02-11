from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.core.files.storage import FileSystemStorage
import cv2
import numpy as np

def homepage_view(request):
    return HttpResponse('Django says: Hello world!')


def home_page(request):
    # получаем все значения модели
    data = Image.objects.all()
    return render(request, 'home_page.html', {'data': data})


def home_page(request):
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()

        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        base_path = 'media/'+filename

        # получение адреса по которому лежит файл
        file_url = fs.url(filename)

        img = cv2.imread(base_path, cv2.IMREAD_COLOR)
        higth_img = img.shape[0]
        weigth_img = img.shape[1]

        #получение координат
        coord = request.POST.get("coordinates")
        coord_lst = coord.split()
        x1 = int(coord_lst[0])
        y1 = int(coord_lst[1])
        x2 = int(coord_lst[2])
        y2 = int(coord_lst[3])

        higth_o = abs(y2-y1)
        weigth_o = abs(x2-x1)
        perimetr = (abs(x2-x1) + abs(y2-y1))*2
        square = abs(x2-x1) * abs(y2-y1)

        r_lst = []
        g_lst = []
        b_lst = []
        for i in range(x1, x2+1):
            for j in range(y1, y2 + 1):
                (b, g, r) = img[i, j]
                r_lst.append(r)
                g_lst.append(g)
                b_lst.append(b)

        avg_r = round(np.average(r_lst))
        avg_g = round(np.average(g_lst))
        avg_b = round(np.average(b_lst))

        return render(request, 'home_page.html', {
            'file_url': file_url,
            'coord': coord,
            'perimetr': perimetr,
            'square': square,
            'higth_img': higth_img,
            'weigth_img': weigth_img,
            'higth_o': higth_o,
            'weigth_o': weigth_o,
            'r_lst': r_lst,
            'g_lst': g_lst,
            'b_lst': b_lst,
            'avg_r': avg_r,
            'avg_g': avg_g,
            'avg_b': avg_b,
        })
    return render(request, 'home_page.html')

