# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
    )

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
    )

    formats = formats_male + formats_female

    first_names_female = (
        'اصيل', 'آلاء', 'آيات', 'ايمان', 'بهجة', 'تمام', 'بشري', 'حياة',
        'خاشعة', 'دانية', 'دعاء', 'زكية', 'نغم', 'لارا', 'زهرة', 'سبأ',
        'ضحى', 'ضياء', 'عالية', 'مريم', 'فداء', 'فرات', 'فردوس',
        'كاملة', 'كوثر', 'هاجر', 'هدى', 'يسرى', 'سجى', 'سلسبيل', 'شهد',
        'جنى', 'اسماءبناتمختلفةومعانيها:', 'ريتاج', 'يارا', 'وصاف',
        'ناردين', 'ميرا', 'مايا', 'مادلين', 'لينا', 'لورا', 'وسجايا',
        'روفيدا', 'ديمه', 'جيلان', 'جوانا', 'ألين', 'لتين', 'تالا',
        'سديم', 'جودي', 'ليان', 'دانة', 'ميار', 'لوجين', 'ربى', 'لورين',
        'ميرال', 'ريتال', 'جوليا', 'جالا', 'جوان', 'راما', 'هايدي',
        'ريفال', 'إلينا', 'أسيل', 'لوليا', 'ليساء', 'ميسون', 'جوين',
        'روبين', 'جمان', 'ميلاء', 'رواء', 'أناهيد', 'بيسان', 'ابتسام',
        'إباء', 'ابتكار', 'ابتهاج', 'ابتهال', 'بوران', 'محمد',
        'بنان', 'بيلسان', 'بتلاء', 'بدرالدّجى', 'تاليا', 'ترف', 'تالا',
        'ترانيم', 'جلنار', 'جميلة', 'جهراء', 'جواهر', 'جوريّة', 'ريمان',
        'ريما', 'ريناد', 'ريفال', 'راما', 'روعة', 'ريما', 'ريم',
        'اعتكاف', 'اعتماد', 'أغاريد', 'افتكار', 'أفراح', 'أفنان',
        'لاما', 'ليم', 'لوليا', 'ريمان', 'أجوان', 'بشرى', 'بلسم',
        'بلقيس', 'بلماء', 'بلند', 'بنان', 'بنفسج', 'بهابهاء', 'بهية',
        'نوره', 'نوف', 'نوال', 'ناديه', 'هدى', 'هناء', 'هيا', 'هند',
        'هنادي', 'وفاء', 'ياسمين', 'يسرى', 'غيداء', 'شادن', 'جود',
        'سلاف', 'جيلان', 'نشوة', 'ريان', 'دارين', '', 'أحلام', 'إخلاص',
        'أروى', 'أريج', 'أزهار', 'أسرار', 'آيات', 'ماذى', 'تولين',
        'هيام', 'ريناد', 'جميلة', 'حلا', 'عتاب', 'كرمة', 'ناهد', 'غوى',
        'ريف', 'بارعة', 'باسمة', 'باهرة', 'بتول', 'بثينة', 'أحمد',
    )

    first_names_male = (
        'تاج', 'تامر', 'تحسين', 'تقي', 'تمّام', 'تميم', 'توفيق', 'ترف',
        'تاج الدّين', 'تقيّ الدّين', 'ثائر', 'ثابت', 'ثامر', 'ثروت',
        'ثقيف', 'ثاقب', 'جابر', 'جاد', 'جاسم', 'جرير', 'جسور',
        'جعفر', 'جلاء', 'جلال', 'جليل', 'جمال', 'جميل', 'جدير',
        'جرّاح', 'جلال الدّين', 'جمال الدّين', 'جهاد', 'حاتم', 'حارث',
        'حازم', 'حافظ', 'حامد', 'حبّاب', 'حسام', 'حسن', 'حسيب',
        'حسين', 'حسني', 'حسنين', 'حقّي', 'حكيم', 'حليم', 'حمّاد',
        'حمدان', 'حمدي', 'حمزة', 'حمود', 'حميد', 'حنبل', 'حنفي',
        'حيّان', 'حيدر', 'حفيظ', 'خاطر', 'خافق', 'خالد', 'خالدي',
        'خلدون', 'خلف', 'خلوصي', 'خليفة', 'خليل', 'خميس', 'خيري',
        'خضر', 'خطيب', 'دؤوب', 'داني', 'داهي', 'داوود', 'دريد',
        'دليل', 'دهمان', 'ديسم', 'ذيب', 'ذكي', 'ذريع', 'رائد',
        'رائف', 'رابح', 'راتب', 'راجح', 'راجي', 'رازي', 'راشد', 'راضي',
        'راغب', 'رامز', 'رامي', 'رامح', 'راني', 'راوي', 'رؤوف', 'رباح',
        'ريّان', 'ربيع', 'رجاء', 'رجائي', 'رجب', 'رخاء', 'رستم',
        'رسمي', 'رشاد', 'رشدي', 'رشيد', 'رضوان', 'رفيق', 'رمحي',
        'رمزي', 'رمضان', 'رهيف', 'روحي', 'رافع', 'رئيس', 'رحيب',
        'رزين', 'راسم', 'رضي', 'زاخر', 'زاكي', 'زاهر', 'زاهي',
        'زايد', 'زبير', 'زغلول', 'زكريا', 'زكي', 'زهدي', 'زهران',
        'زهير', 'زياد', 'زيد', 'زيدان', 'زين', 'سائد', 'ساجد',
        'سخاء', 'ساجي', 'ساطع', 'سالم', 'سامح', 'ساهر', 'سامر',
        'سامي', 'ساهد', 'سراج', 'سرحان', 'سرور', 'سعد', 'سعدون',
        'سعدي', 'سعود', 'سعيد', 'سفيان', 'سفير', 'سلام', 'سلطان',
        'سلمان', 'سليمان', 'سموح', 'سمير', 'سنان', 'سنام', 'سهل',
        'سهوان', 'سهيل', 'سيّد', 'سليم', 'سراج الدّين', 'سيفالدّين',
        'شادي', 'شافع', 'شاكر', 'شامخ', 'شامل', 'شبلي', 'شبيب',
        'شدّاد', 'شريف', 'شعبان', 'شعيب', 'شفيع', 'شعلان', 'شكري',
        'شكيب', 'شهب', 'شهاب', 'شهم', 'شهير', 'شوقي', 'شجاع', 'شاطر',
        'شيّق', 'صائب', 'صابر', 'صاحب', 'صادح', 'صادق', 'صارم',
        'صافي', 'صالح', 'صامد', 'صباح', 'صبحي', 'صبري', 'صبور',
        'صبيح', 'صخر', 'صدقي', 'صدّام', 'صدّاح', 'صعب', 'صقر',
        'صلاح', 'صنديد', 'صهيب', 'صدر الدّين', 'صلاح الدّين', 'ضاحك',
        'ضاحي', 'ضحّاك', 'ضرغام', 'ضياء', 'ضيائي', 'ضياءالدّين',
        'طائع', 'طائف', 'طائل', 'طارق', 'طالب', 'طامح', 'طاهر',
        'طبّاع', 'طريف', 'طلال', 'طلعت', 'طموح', 'طه', 'طيّب',
        'طيّع', 'ظافر', 'ظبي', 'ظريف', 'ظهير', 'ظاعن', 'ظاهر',
        'عائد', 'عابد', 'عادل', 'عارف', 'عاصم', 'عاطف', 'عاقل',
        'عاكف', 'عالم', 'عامر', 'عبّاس', 'عبّود', 'عتريس', 'عتيد',
        'عربي', 'عثمان', 'عدلي', 'عدنان', 'عدوي', 'عرفات', 'عرفه',
        'عرفان', 'عزاز', 'عزّت', 'عزمي', 'عصام', 'عصمت', 'عطاء',
        'عفيف', 'عقيل', 'علاء', 'علّام', 'علوان', 'علي', 'عماد',
        'عمّار', 'عمر', 'عمران', 'عمرو', 'عمير', 'عاتب', 'عتيق',
        'عذب', 'عزيز', 'عبد الحقّ', 'عبدالله', 'عبدالرّحمن',
        'عزّالدّين', 'علاءالدّين', 'علم الدّين', 'عبد الإله', 'مُتعب',
        'عبد الباري', 'عبد الباقي', 'عبد التّواب', 'عبد الجبّار',
        'عبد الجليل', 'عبد الحفيظ', 'عبد الحكيم', 'عبد الحليم',
        'عبد الحيّ', 'عبد المحيي', 'عبد الخالق', 'عبد الرّزاق', 'هزار',
        'عبد الرّشيد', 'عبد الرّحمن', 'عبد الرّحيم', 'عبد الرّؤوف',
        'عبد السّميع', 'عبد الشّكور', 'عبد الصّمد', 'عبد العليم',
        'عبد الغفّار', 'عبد الغفور', 'عبد القادر', 'مهنّد', 'نزيه',
        'عبد القدّوس', 'عبد القهّار', 'عبد الكريم', 'عبد اللطيف',
        'عبد المجيد', 'عبد المولى', 'عبد العزيز', 'عبد السّلام',
        'عبد الملك', 'عبد الواحد', 'عبد الغني', 'غازي', 'غالب',
        'غالي', 'غانم', 'غزوان', 'غسّان', 'غطفان', 'غزير', 'غامد',
        'فائق', 'فاتح', 'فاخر', 'فادي', 'كامل', 'مصعب', 'ممتاز',
        'فرج', 'فارس', 'فارع', 'فاروق', 'فاضل', 'فالح', 'فايد', 'فتوح',
        'فتحي', 'فخر', 'فخري', 'فداء', 'فدائي', 'فراس', 'فرج', 'فرحان',
        'فرزدق', 'فضل', 'فطين', 'فكري', 'فلاح', 'فهد', 'فهمي', 'فؤاد',
        'فوّاز', 'فوزي', 'فضل', 'فيّاض', 'فيصل', 'فخر الدّين', 'قاسم',
        'قاصد', 'قانت', 'قائد', 'قحطان', 'قدري', 'قصي', 'قنوع', 'قيس',
        'قبس', 'قصيد', 'قطب', 'قطز', 'كارم', 'كاسر', 'كاشف', 'كاظم',
        'كايد', 'كافور', 'كتوم', 'كرم', 'كريم', 'كسّاب', 'كمال', 'كنار',
        'كنعان', 'كنان', 'كبير', 'كليم', 'لبيب', 'لبيد', 'لطفي', 'لطوف',
        'لفيف', 'لقمان', 'لقاء', 'لؤي', 'لهفان', 'ليث', 'لمّاح', 'مأمون',
        'ماجد', 'مازن', 'مالك', 'ماهر', 'محمّد', 'مُتوكّل', 'مُتولي',
        'مُتيّم', 'مجد', 'مجاهد', 'مَجدي', 'محجوب', 'محسن', 'محفوظ',
        'محمود', 'مختار', 'مخلص', 'مُخيمر', 'مدحت', 'مراد', 'مرادي',
        'مرتجي', 'مرتقي', 'مرزوق', 'مرسال', 'مرتضي', 'مُرسي', 'مرشد',
        'مُرضي', 'مرعي', 'مروان', 'مزهر', 'مسرور', 'مُسعف', 'مَسعد',
        'مسعود', 'مسلم', 'مشرف', 'مشرق', 'مشفق', 'مصباح', 'مصطفى',
        'مُصلح', 'مطاوع', 'مظهر', 'مُعتز', 'معتوق', 'معزّ', 'معمّر', 'معن',
        'معين', 'مفيد', 'مقداد', 'مقدام', 'مكّي', 'مكرّم', 'ملهم', 'يونس',
        'ممدوح', 'مُناضل', 'مناف', 'مُنذر', 'منيف', 'منتصر', 'مُنجد',
        'منسي', 'منصور', 'مُنير', 'منيب', 'منيع', 'مهدي', 'مهران',
        'مهيب', 'موسى', 'موفّق', 'مؤمن', 'مؤنس', 'مؤيّد', 'ميّاد', 'مياس',
        'ميسور', 'ميمون', 'ميثاق', 'معارف', 'محييالدّين', 'مشاري',
        'نائل', 'ناجح', 'ناجي', 'نادر', 'نادي', 'ناصر', 'ناضر', 'ناصيف',
        'ناظم', 'ناعم', 'نافذ', 'نافع', 'نبهان', 'نبيل', 'نبيه', 'نبراس',
        'نورالحقّ', 'نجدت', 'نجوان', 'نجيب', 'نديم', 'نذير', 'نزار',
        'نسيب', 'نشأت', 'نصر', 'نضال', 'نصري', 'نصور', 'نصوح', 'نظام',
        'نظمي', 'نعيم', 'نعمان', 'نمر', 'نوّاف', 'نوح', 'نوّار', 'نور',
        'نورس', 'نشوان', 'نوري', 'نيازي', 'ناصر الدّين', 'نصر الدّين',
        'نور الدّين', 'نجم الدّين', 'هادي', 'هاشم', 'هاني', 'هايل',
        'هلال', 'هلالي', 'همام', 'هيكل', 'هيمان', 'هيثم', 'وائل', 'واثق',
        'وادع', 'واصف', 'واصل', 'وثّاب', 'وجدي', 'وجيه', 'وحيد', 'ودود',
        'وديع', 'وريد', 'وسام', 'وسيم', 'وسيل', 'وصفي', 'وضّاح', 'وفائي',
        'وفيق', 'وليد', 'وليف', 'ياسر', 'يافع', 'ياقوت', 'يانع', 'يحيى',
        'يزيد', 'يسار', 'يسري', 'يعرب', 'يعقوب', 'يقين', 'يمام', 'يوسف',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'الخالدي', 'البديري', 'الشهابي', 'العفيفي', 'جزار',
        'الخطيب بني جماعة الكناني', 'الدجاني', 'الغوانمة', 'جار الله',
        'السروري', 'الامام', 'النقيب', 'المفتي', 'ابو السعود',
        'الفتياني', 'العلمي', 'بو مدين', 'نسيبة', 'النشاشيبي', 'العسلي',
        'الحسيني', 'الجاعوني', 'درويش', 'الأنصاري', 'جودة', 'النمري',
        'قطينة', 'الداودي', 'العارف', 'رصاص', 'البخاري', 'كمال',
        'الترجمان الصالح', 'غنيم', 'المؤقت', 'شتية', 'شرف', 'نور الدين',
        'الشعباني', 'الأيوبي', 'الجبشة', 'هندية', 'البشيتي', 'الوعري',
        'الموسوس', 'المظفر', 'الترهي', 'البغدادي', 'الهدمي', 'البامية',
        'الكلغاصي', 'اليوزباشي', 'المتولي', 'اسطمبولي', 'الألجاوي',
        'معتوق', 'حب رمان', 'القرجولي', 'نجم', 'طه', 'عبده', 'سموم',
        'نجيب', 'غوشة', 'اهرام', 'قرش', 'الكالوتي', 'حجازي', 'زحيكة',
        'جعفر', 'ازحيمان', 'الحواش', 'القضماني', 'طوطح', 'الشاويش',
        'بدرية', 'ابو الحاج', 'البيطار', 'صيام', 'قليبو', 'ارناؤوط',
        'الشرفاء', 'الحلاق', 'المملوك', 'السمان', 'طقش', 'وهبة',
        'عبد اللطيف', 'طزيز', 'السيفي', 'عويضة', 'القطب', 'الطحان',
        'النجار', 'القباني', 'عكاوي', 'الديسي', 'الزماميري', 'التوتنجي',
        'الحلواني', 'القزاز', 'الماني', 'الدقاق', 'الشامي', 'سوميرة',
        'ابو عيد', 'الخلفاوي', 'الدسوقي', 'المغربي', 'أفغاني', 'مراد',
        'زلاطيمو', 'سرندح', 'مشعشع', 'بحمدوني', 'بعلبكي', 'صيداوي',
        'صيداني', 'طرابلسي', 'جزيني', 'بيروتي', 'عرموني', 'متني',
        'شويفاتي', 'مزرعاني', 'بتروني', 'جبيلي', 'اميوني', 'زحلاوي',
        'الساحلي', 'القاعي', 'القلموني', 'البيسار القعقور', 'إياد',
        'الأزد', 'الأشراف', 'السادة', 'الأوس', 'أشجع', 'ألمع', 'أنمار',
        'بنو الأحمر', 'بنو الأحمر بن الحارث', 'بنو الأسمر', 'بنو أسد',
        'بنو أمية', 'أكلب', 'بنو النجار', 'البقوم', 'أولاد بوعزيز',
        'بارق', 'باهلة', 'بجيلة', 'بكر بن عبد مناة', 'بكر بن وائل',
        'بديرية', 'بلغازي', 'بلقرن', 'بلي', 'بيرقدار', 'بني بيات',
        'بكيل', 'ترابين', 'تغلب بن وائل', 'تميم', 'تنوخ', 'ثقيف',
        'الجعليين', 'جرهم', 'جديس', 'جذام', 'جهينة',
        'الحجر بن الهنوء بن الأزد', 'الحداء', 'الحكم بن سعد العشيرة',
        'بنو الحارث بن كعب', 'حرب', 'بنو حنيفة', 'حاشد', 'حميضة',
        'حمير', 'حوالة', 'الحويطات', 'الخزرج', 'بنو خالد', 'خثعم',
        'خزاعة', 'خندف', 'خولان', 'الدليم', 'الدواسر', 'بنو الدئل',
        'دوبلال', 'بنو ذي أصبح', 'راجح', 'بني رشيد', 'ربيعة', 'الرباب',
        'الرباطاب', 'السادة الراويون', 'الزرقان', 'زبيد', 'أولاد زيان',
        'بنو زيد', 'زهران', 'السهول', 'بنو سعد بن بكر',
        'بنو سعد بن ليث بن بكر', 'سليم', 'سبيع', 'الشايقية', 'الشحوح',
        'بنو شعبة', 'شمران', 'بنو شهر', 'بنو شيبان', 'بنو شيبة', 'شمر',
        'شهران', 'بنو صخر', 'بنو ضمرة', 'ضبيعة', 'طسم', 'طيء', 'الظفير',
        'عجرمة (العجارمة)', 'العجمان', 'العقيدات', 'العوازم', 'العوالق',
        'بنو العريج', 'عاملة', 'بنو عبس', 'بنو عجل', 'بنو عدي',
        'بنو عمرو', 'عامر بن صعصعة', 'عبد القيس', 'عتيبة', 'عدوان',
        'عذرة', 'عسير', 'عليان', 'عنز بن وائل', 'عنزة', 'عنس', 'عضل',
        'بني عطية', 'غامد', 'غطفان', 'بنو فراس', 'فراهيد', 'فهم',
        'القواسم', 'قحطان', 'قريش', 'قضاعة', 'قيس عيلان', 'بنو كنز',
        'الكواهلة', 'بنو كلب', 'كنانة', 'الكبابيش', 'كندة', 'كهلان',
        'الكثيري', 'بنو لام', 'لخم', 'بنو ليث', 'المرازيق', 'المنتفق',
        'الموركة', 'المهرة', 'بنو مالك', 'بنو معقل', 'بنو مهدي',
        'مزينة', 'مذحج', 'مرازيق البقوم', 'مضر', 'مطير', 'ميرفاب',
        'النمر', 'نهد', 'بني هاجر', 'بنو هاشم', 'بنو هلال',
        'قبيلة هذيل البقوم', 'هذيل', 'همدان', 'هوازن', 'بنو ياس',
        'بنو يعلى', 'يافع', 'يشكر',
    )

    prefixes_female = (
        'السيدة', 'الآنسة', 'الدكتورة', 'الأستاذة', 'المهندسة',
    )
    prefixes_male = ('السيد', 'المهندس', 'الدكتور', 'الأستاذ',)
