{%- macro sidebyside(titles=['Unix', 'Windows']) -%}
    <div class="row side-by-side-commands">
        {%- for title in titles -%}
            <div class="col">
                <h4>{{ title }}</h4>
{%- filter markdown() -%}
```{%- if title.lower().startswith('win') -%}dosvenv{%- else -%}console{%- endif -%}
{{ caller() | extract_part(loop.index0, '---') | dedent }}
```
{%- endfilter -%}
            </div>
        {%- endfor -%}
    </div>
{%- endmacro -%}

{%- if var('pyladies') -%}
{% set purpose = 'PyLadies' %}
{% set dirname = 'pyladies' %}
{%- else -%}
{% set purpose = 'Python' %}
{% set dirname = 'naucse-python' %}
{%- endif -%}


# سطر الأوامر (Command line)

ستوضح الخطوات التالية كيفية استخدام النافذة السوداء التي يستخدمها جميع الهاكرز. قد تبدو مخيفة بعض الشيء في البداية، لكنها في الواقع مجرد موجه ينتظر الأوامر منك.

ما هو سطر الأوامر؟
النافذة، التي تسمى عادةً *سطر الأوامر (command line)* أو *واجهة سطر الأوامر (command-line interface)*، هي تطبيق نصي لعرض ملفاتك على جهاز الكمبيوتر الخاص بك ومعالجتها وتلاعبها. إنه يشبه إلى حد كبير مستكشف Windows أو Finder (Mac)، ولكن بدون الواجهة الرسومية.
أسماء أخرى لسطر الأوامر هي:
*cmd*, *CLI*, *prompt*, *console* أو *terminal*.

كيف يمكنني فتحه؟

* Windows (English): ابدأ (Start ) ← اكتب "cmd" ← موجه الأوامر (Command prompt)
* Windows (إصدارات قديمة): قائمة ابدأ (Start ) ← جميع البرامج (All programs) ← ملحقات(Accessories) ← موجه الأوامر (Command prompt)
* macOS (English): التطبيقات ← المرافق ← Terminal
* Linux (KDE): القائمة الرئيسية ← ابحث عن Console
* Linux (GNOME): Super ← ابحث عن Terminal

إذا كنت لا تعرف ماذا تفعل، يمكنك تجربة Google أو سؤال المدرب.

عندما تفتح سطر الأوامر، يجب أن ترى نافذة بيضاء أو سوداء تنتظر أمرك.
سيتم إضافة بادئة لكل أمر برمز `$` أو `<` (حسب نظام التشغيل الخاص بك)
ومسافة واحدة، لكن لا يتعين عليك كتابة هذا الموجه.



{% call sidebyside(titles=['Unix (Linux, macOS)', 'Windows']) %}
$
---
>
{% endcall %}

تختلف مجموعة الأوامر الخاصة بسطر الأوامر قليلاً من نظام تشغيل لآخر، لذا تأكد من اتباع التعليمات الخاصة بنظام التشغيل الخاص بك.


> [note] حجم الخط(Font size) (Windows)
> إذا كان الخط صغيرًا جدًا، يمكنك النقر على أيقونة النافذة الصغيرة في الزاوية العلوية اليمنى. ثم اختر الخصائص (Properties) وابحث عن  علامة التبويب الخط (Font) حيث يمكنك تعيين حجم خط مختلف.
>
> {{ figure( img=static('windows-cmd-properties.png'), alt='Screenshot of command line window', ) }}
>
> في أنظمة التشغيل الأخرى، يمكنك تجربة:
> <kbd>Ctrl</kbd>+<kbd>+</kbd> و
> <kbd>Ctrl</kbd>+<kbd>-</kbd> (+ Shift).




سنبدأ بأمر بسيط للغاية.
اكتب `whoami` (*من أنا؟*)
واضغط على <kbd>Enter</kbd>.
سيتم عرض معرف المستخدم الخاص بك. على سبيل المثال، على جهاز الكمبيوتر الخاص بـ Alex، يبدو الأمر كما يلي:


{% call sidebyside() %}
$ whoami
Alex
---
> whoami
PCname\Alex
{% endcall %}

## المجلد الحالي (Working Directory)

يعمل سطر الأوامر دائمًا من **مجلد (Directory)** معين.

يمكننا طباعة **المجلد (Directory)** الحالي باستخدام الأمر `pwd` (Linux, MacOS)

أو `cd` (Windows). `pwd` تعني *طباعة المجلد الحالي (Print Working Directory)* و `cd` تعني *المجلد الحالي (Current Directory)*

{% call sidebyside() %}
$ pwd
/home/Alex/
---
> cd
C:\Users\Alex
{% endcall %}

غالبًا ما يتم عرض **المجلد (Directory)** الحالي أيضًا قبل علامة `$` أو `>`، ولكن من الجيد معرفة هذا الأمر في حالة ضياعك أو إذا كان عليك العمل على جهاز كمبيوتر معروضًا عليه شيء مختلف قبل علامة `$`.

## ماذا يوجد في هذا **المجلد (Directory)**؟

الأمر `ls` أو `dir` (*قائمة* أو *مجلد*)
سيعرض لنا ما يوجد في **المجلد (Directory)** الحالي: جميع الملفات
والمجلدات الفرعية.

{% call sidebyside() %}
$ ls
Applications
Desktop
Downloads
Music
…
---
> dir
 Directory of C:\Users\Alex
05/08/2014 07:28 PM <DIR>  Applications
05/08/2014 07:28 PM <DIR>  Desktop
05/08/2014 07:28 PM <DIR>  Downloads
05/08/2014 07:28 PM <DIR>  Music
…
{% endcall %}


## تغيير **المجلد (Directory)** الحالي

يمكنك تغيير **المجلد (Directory)** الحالي باستخدام الأمر `cd` (*تغيير المجلد*) -
لجميع أنظمة التشغيل (في Windows، إذا لم تحدد أي شيء بعد `cd`، فإن الأمر
يطبع **المجلد (Directory)** الحالي كما قلنا سابقًا)
لذا بعد `cd` يجب أن نكتب اسم **المجلد (Folder)** الذي نريد الانتقال إليه.
لا تنسى التحقق مما إذا كنت قد نجحت.

إذا كنت تستخدم Linux أو macOS، كن حذرًا - هذه الأنظمة حساسة لحالة الأحرف،
لذا فإن `Desktop` و `desktop` مجلدات مختلفة!


{% call sidebyside() %}
$ cd Desktop
$ pwd
/home/Alex/Desktop
---
> cd Desktop
> cd
C:\Users\Alex\Desktop
{% endcall %}

> [note] ملاحظة لمستخدمي Windows
> إذا قمت بتغيير **المجلد (Directory)** إلى قرص مختلف (إلى `D:` من `C:`)
> يجب عليك إدخال اسم القرص (`D:`) كأمر خاص قبل
> إدخال `cd`.

## إنشاء **مجلد (Directory)**

ما رايك بإنشاء **مجلد (Directory)** تدريب على سطح المكتب الخاص بك؟ يمكنك القيام بذلك باستخدام الأمر
`mkdir` (*إنشاء مجلد*).
بعد ذلك، اكتب اسم **المجلد (Folder)** الذي تريد إنشاؤه -
في حالتنا `practice`.


{% call sidebyside() %}
$ mkdir practice
---
> mkdir practice
{% endcall %}

الآن، انظر إلى سطح المكتب أو أي برنامج اخر
لتصفح **المجلدات (Folders)**، وتحقق مما إذا تم إنشاء **المجلد (Folder)**!

## المهمة

في **المجلد (Folder)** الجديد `practice` الخاص بك، حاول إنشاء **مجلد (Folder)** فرعي `test` وتحقق
مما إذا تم إنشاؤه.

يمكن للأوامر `cd` و `mkdir` و `ls` أو `dir` مساعدتك.


{% filter solution %}
{% call sidebyside() %}
$ cd practice
$ mkdir test
$ ls
test
---
> cd practice
> mkdir test
> dir
05/08/2014 07:28 PM <DIR>  test
{% endcall %}
{% endfilter %}


## التنظيف

لا نريد ترك فوضى، لذلك دعونا نزيل كل ما قمنا به حتى تلك النقطة.

لكن لا يمكنك حذف **المجلد (Folder)** الذي أنت فيه حاليًا.
أولاً، نحتاج إلى العودة إلى سطح المكتب. لا يمكننا استخدام `cd Desktop` لأننا في **المجلد (Folder)** الحالي، لا يوجد سطح مكتب.
لذا يجب أن نذهب إلى **المجلد (Folder)** الرئيسي الذي يحتوي على **المجلد (Folder)** الذي أنت فيه حاليًا.

نقطتان **"..**" تمثلان **المجلد (Folder)** الرئيسي.

{% call sidebyside() %}
$ pwd
/home/Alex/Desktop/practice
$ cd ..
$ pwd
/home/Alex/Desktop
---
> cd
C:\Users\Alex\Desktop\practice
> cd ..
> cd
C:\Users\Alex\Desktop
{% endcall %}

## حذف **المجلد (Directory)**

الآن، حان الوقت لحذف **المجلد (Directory)** `practice`.
لفعل ذلك، استخدم `rm` أو `rmdir`
(*إزالة* أو *إزالة مجلد*).


> [warning] تحذير!
> لا يحتوي سطر الأوامر على سلة مهملات أو زر تراجع! سيتم حذف كل شيء نهائيًا.
>
> في كل مرة، تأكد من أنك تقوم بحذف **المجلد (Directory)** الصحيح.


في Unix، يجب عليك كتابة `rm -rv` (ناقص، `r`، `v`). يقوم المعامل بحذف كل شيء
(`r` - *تكراري*) داخل **المجلد (Directory)**، ويطبع معلومات تخبرك (`v` - *مفصل*)
بما يفعله الأمر.

في Windows، يجب عليك أيضًا إضافة مفتاح إلى الأمر `rmdir` لحذف كل شيء داخل
**المجلد (Directory)**. هنا، المفتاح هو `/S`.

`rmdir` بدون المفتاح الإضافي يحذف فقط **المجلد (Directory)** الفارغ.

{% call sidebyside() %}
$ pwd
/home/Alex/Desktop
$ rm -rv practice
removed directory: ‘practice’
---
> cd
C:\Users\Alex\Desktop
> rmdir /S practice
practice, Are you sure <Y/N>? Y
{% endcall %}


## ملخص الأوامر الأساسية

هناك جدول للأوامر الأساسية التي يمكنك استخدامها كمرجع لبداية رحلتك المذهلة!

| يونكس (Unix) | ويندوز (Windows) | الوصف | مثال |
|---|---|---|---|
| `cd` | `cd` | تغيير **المجلد (Directory)** | `cd test` |
| `pwd` | `cd` | عرض **المجلد (Directory)** الحالي | `pwd` <br> `cd` |
| `ls` | `dir` | قائمة **المجلدات (Directories)**/الملفات | `ls` <br> `dir` |
| `cp` | `copy` | نسخ ملف | `cp original.txt copy.txt` <br> `copy original.txt copy.txt` |
| `mv` | `move` | نقل ملف | `mv old.txt new.txt` <br> `move old.txt new.txt` |
| `mkdir` | `mkdir` | إنشاء **مجلد (Directory)** جديد | `mkdir test` |
| `rm` | `del` | حذف ملف | `rm test.txt` <br> `del test.txt` |
| `rm -rv` | `rmdir /S` | حذف **مجلد (Directory)** | `rm -rv testdir` <br> `rmdir /S testdir` |
| `exit` | `exit` | إغلاق النافذة (اختياريًا `CTRL+D` يؤدي نفس الشيء) | `exit` |

<br />

هناك بالطبع العديد من الأوامر الأخرى المتاحة في سطر الأوامر الخاص بك.

يمكن تشغيل بعض البرامج التي قمت بتثبيتها على الكمبيوتر المحمول الخاص بك من سطر الأوامر - عادةً عن طريق كتابة أسمائها.

جرب على سبيل المثال - `firefox`, `notepad`, `safari`, أو `gedit`.

{% if var('coach-present') -%}
إذا لم ينجح الأمر، اسأل مدربك وقد يساعدك في العثور على أمر مثال يعمل.
{%- endif %}

سنستخدم أوامر/برامج مثل `python` و `git` كثيرًا.

## الخروج

الآن يمكنك تجربة أمر آخر - الأمر الذي يغلق نافذة سطر الأوامر - `exit`.
اختياريًا أيضًا `CTRL+D` يؤدي نفس الشيء.

يجب أن يعمل بنفس الطريقة في جميع أنظمة التشغيل.

سنستخدم `$` للإشارة إلى أوامر Linux/macOS (في الواقع، لأنظمة التشغيل المستندة إلى يونكس)
و `<` للإشارة إلى أوامر Windows لبقية الدورة التدريبية.
هذا هو الاتفاقية في معظم المواد والدروس التعليمية التي ستجدها.