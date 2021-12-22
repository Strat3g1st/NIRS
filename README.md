# 1. Методы, взятые для исследования:

DFN: https://github.com/hughplay/DFNet

CRA: https://github.com/Atlas200dk/sample-imageinpainting-HiFill

HII: https://github.com/GouravWadhwa/Hypergraphs-Image-Inpainting

Заменить все test.py в этих методах на redacted версии из репозитория НИРС. Для запуска использовать параметры из DFN_param.txt, HII_param.txt, CRA_param.txt. Причем CRA_param.txt - это переменные в самом исходном коде test.py. Для HII использованные параметры в виде conf_<name>.txt - прилагаются в репозитории. Сгенерировать заново с заданными путями их можно с помощью conf_gen.py В случае CRA использовался код в папке GPU_CPU.

Везде запускал на CPU, для GPU с CUDA скорее всего правки в коде могут не сработать, учитывая ветки if-else. Но в целом можно отметить, что довольно медленно работает только CRA.

Pretrained models
Для DFNet взять places2: https://drive.google.com/drive/folders/1lKJg__prvJTOdgmg9ZDF9II8B1C3YSkN
Для CRA взять: https://github.com/Atlas200dk/sample-imageinpainting-HiFill/tree/master/GPU_CPU/pb
Для HII взять все отсюда: https://drive.google.com/drive/folders/1dk1zSm1FxZVaafOtvoud8aAdZ6Ubs4oU 

# 2. Софт
В generate_database.py можно подправить ссылку на папку с изображениями из images.7z (отметил комментарием) 
В config.py указать в abs_path папку, где будет находится БД изображений в виде системы подпапок (отметил комментарием)
Для генерации БД с нуля запускать generate_database.py. 
Для повторной генерации при изменении каких-то параметров масок или изображений image_gen.py, 
либо можно удалить папку и запустить generate_database.py.

В config.py masked_color = 0 - черный цвет будет отвечать за вырез фрагмента, non_masked_color = 255 - белый цвет за нетронутую область изображения. 
Для DFNet и CRA HiFill эти переменные должны быть таких значений, а для HII - поменять местами и заново прогенерить БД 
(генерируется не так долго, минут пять-десять и запускать). 

На данный момент маски генерируются одинакового размера, но это просто потому что сами изображения такие, все сначала делалось для изображений разного размера.


# 3. БД

Исходные изображения в images.7z. Сама БД с фрагментациями и масками автоматически сгенерируется, 
если способами в пункте 2 этого сообщения подправить на свои пути к папкам, установить требуемые библиотеки и запустить. Сама БД в DB.z
