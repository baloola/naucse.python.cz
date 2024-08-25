Markdown
# تثبيت بايثون على ماك


أولاً، تحقق في **سطر الأوامر (command line)** أو **المحطة (terminal)** الخاصة بك
إذا لم يكن لديك بالفعل بايثون 3 مثبتًا.
افتح المحطة واكتب فيها:

```console
$ python3 --version
```

إذا ظهر "بايثون" ورقم الإصدار (مثل Python 3.8.2) وكان الإصدار أعلى من أو يساوي 3.8، فإن كل شيء على ما يرام، يرجى المتابعة مع
القسم التالي.

إذا لم يكن كذلك، فيرجى تثبيت Homebrew الذي يجعل تثبيت التطبيقات والوحدات أسهل بكثير.

تحقق أولاً مما إذا كان Homebrew مثبتًا بالفعل عن طريق:

```Shell
brew -v
```

إذا لم يرد الأمر السابق بإصدار مثبت من Homebrew، فقم بتثبيته عن طريق إدخال هذا الأمر في سطر الأوامر (command line) أو المحطة (terminal):

```Shell
$ /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"  

```

ثم يمكنك فقط إدخال هذا الأمر:

```Shell
$ brew install python3
```

يجب أن يؤدي كتابة python3 --version مرة أخرى إلى إرجاع إصدار قيد الاستخدام من بايثون.

ملاحظة: - إذا كان لديك إصدارات أقدم من نظام التشغيل Mac OS X - على سبيل المثال 10.10.x، فلن تتوفر لك أحدث إصدارات Python و VSCode.

ستحتاج إلى تثبيت إصدار أقدم من كليهما يدويًا.

`Python`: https://legacy.python.org/download/mac  سيقودك بالتأكيد إلى حل.

VS Code: على سبيل المثال، يمكن أن يحل إصدار يناير 2021 من VS Code ذلك - راجع https://stackoverflow.com/a/67763370/7875133 للحصول على مزيد من التفاصيل.