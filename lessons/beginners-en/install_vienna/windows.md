# تثبيت بايثون لنظام التشغيل ويندوز

توجه إلى [موقع بايثون](https://www.python.org/downloads/) وقم بتنزيل "أحدث إصدار مستقر من بايثون"( `latest stable version of Python`). في وقت كتابة هذه المواد، فهو `بايثون 3.12.5`.

كيف تعرف مُثبِّت النظام(installer) الصحيح لك؟

إذا كان جهاز الكمبيوتر الخاص بك يعمل بنظام ويندوز 64 بت، فقم بتنزيل *Windows installer (64-bit)*.
إذا كان نظام التشغيل ويندوز الخاص بك 32 بت فقط، فقم بتنزيل *Windows installer (32-bit)*.

> [ملاحظة]
>
> إذا كنت لا تعرف إصدار ويندوز الذي لديك، فما عليك سوى فتح **ابدأ** (**Start**)، والبحث عن **النظام**(**System**) وفتح **معلومات النظام**(**System information**).
>
> {{ figure(
    img=static('windows_32v64-bit.png'),
    alt='Windows version',
) }}

بعد ذلك يمكنك تشغيل المُثبِّت.


> [تحذير]  في البداية، تأكد من تحديد**Install launcher for all Users** وأيضًا مهم جدًا: **Add Python 3.12 to PATH**.


(إذا لم يكن لديك حقوق المسؤول، فلا تحدد *Install launcher for all Users*.)

{{ figure(
    img=static('windows_add_python_to_path.png'),
    alt='python installation,
> ) }}

ثم انقر فوق **Install now** واتبع التعليمات.

