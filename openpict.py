from PIL import Image
import title as T

def openpic(obj1,obj2,obj3):
    num = T.title(obj1,obj2,obj3)

    for i in num:
        img = Image.open(''.join(r'C:\Users\Вадим\Downloads\kadid10k\kadid10k\images\\' +i )) #Путь к картинкам
        img.show()


#Запуск
openpic('1','3-5','5')