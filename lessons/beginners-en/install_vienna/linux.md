

# تثبيت بايثون على لينكس
تثبيت بايثون على لينكس سهل للغاية.
الجزء الصعب الوحيد قد يكون وجود العديد من **التوزيعات (distributions)** التي تحتاج إلى **أوامر تثبيت (installation commands)** مختلفة.

## بايثون 3

أولاً، تحقق في **سطر الأوامر (command line)** أو **المحطة (terminal)** الخاصة بك
إذا لم يكن لديك بالفعل بايثون 3 مثبتًا.
افتح المحطة واكتب فيها:

```console
$ python3 --version
```

إذا ظهر "بايثون" ورقم الإصدار (مثل Python 3.8.2) وكان الإصدار أعلى من أو يساوي 3.8، فإن كل شيء على ما يرام، يرجى المتابعة مع
القسم التالي.

إذا ظهر "بايثون" وإصدار أقل من 3.8، اسألنا عن كيفية المتابعة.

إذا ظهر `bash: python3: command not found` أو شيء مشابه، فسيتعين عليك تثبيت بايثون 3.
الأمر يعتمد على التوزيع (distribution) الخاص بك.

* Fedora:
  {% filter markdown(inline=True) %}
  ```console
  $ sudo dnf install python3
  ```
  {% endfilter %}
* Ubuntu:
  {% filter markdown(inline=True) %}
  ```console
  $ sudo apt-get install python3
  ```
  {% endfilter %}