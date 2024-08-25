{% set editor_name = 'VSCode' %}
{% set editor_url = 'https://code.visualstudio.com/' %}
{% extends lesson.slug + '/_base.md' %}

{% block name_gen %} VSCode {% endblock %}

{% block setup %}

# تثبيت إضافة بايثون (Python extension) لـ VSCode

بالنسبة لدورة المبتدئين، يجب عليك تثبيت `Python extension` لـ VSCode.

عند فتح VSCode، في الشريط الجانبي الأيسر، اختر `Extensions` (Ctrl + Shift + X) مع رمز المكعبات الأربعة.

بعد ذلك، في شريط البحث العلوي لـ Extensions، ابحث عن "Python" وفي قائمة الإضافات التي تظهر، حدد وقم بتثبيت الحزمة الأولى المقترحة: `Python` - من تأليف Microsoft. يمكنك تثبيت الحزمة بالنقر فوق الزر الصغير "Install" الموجود في أسفل العنصر في القائمة أو بعد النقر على العنصر في اللوحة المفتوحة حديثًا وفي أعلى الصفحة، يجب أن يكون هناك زر صغير "install".


> [note]
> تعمل التحكم بالمسافات التلقائية(indentation) وتلوين الكود المطلوب (لأغراضنا) فقط عندما يكون الملف يحتوي على امتداد `.py`.
> لذلك من الأفضل أن تحفظ الملف الذي تم إنشاؤه حديثًا بامتداد `.py` في أقرب وقت ممكن.

{% endblock %}
