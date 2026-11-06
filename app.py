<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة كفاءة الوطنية الموحدة للتعلم والتطوير المهني - دولة قطر</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        qatar: {
                            maroon: '#8A1538',       /* العنابي القطري الرسمي */
                            maroonDark: '#560D23',   /* عنابي داكن للرؤوس والبطاقات */
                            maroonDeep: '#3B0818',   /* خلفيات داكنة جداً */
                            maroonLight: '#A6264C',  /* عنابي فاتح للتدرجات */
                            maroonSoft: '#FDF2F4',   /* خلفيات وردية ناعمة */
                            mint: '#AAD2C3',         /* الأخضر الفاتح المعتمد */
                            mintDark: '#184E42',     /* أخضر داكن */
                            gold: '#D4AF37',         /* الذهبي للشارات والاعتمادات */
                            goldDark: '#AA820A',
                            slate: '#1E293B'
                        }
                    },
                    fontFamily: {
                        sans: ['Arial', 'Tahoma', 'sans-serif']
                    }
                }
            }
        }
    </script>
    <style>
        body {
            font-family: Arial, Tahoma, sans-serif;
            background-color: #F8FAFC;
        }
        .maroon-gradient {
            background: #F8FAFC;
        }
        .maroon-card-gradient {
            background: #F8FAFC;
        }
        .gold-badge {
            background: #F8FAFC;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6 px;
            height:6 px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #F1F5F9;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #CBD5E1;
            border-radius: 4 px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
            background: #8A1538;
        }
    </style>
</head>
<body class="text-slate-800 min-h-screen flex flex-col antialiased">

    <!-- 1. شريط التوثيق السيادي الحكومي -->
    <div class="bg-qatar-maroonDark text-white py-1.5 px-4 sm:px-8 text-xs flex justify-between items-center border-b border-qatar-maroon/60">
        <div class="flex items-center space-x-3 space-x-reverse">
            <span class="flex items-center gap-1.5 font-bold">
                <i class="fa-solid fa-landmark text-qatar-gold"></i>
                <span>دولة قطر | ديوان الخدمة المدنية والتطوير الحكومي - معهد الإدارة العامة</span>
            </span>
            <span class="hidden md:inline-block text-white/40">|</span>
            <span class="hidden md:inline-flex items-center gap-1 text-white/80">
                <i class="fa-solid fa-shield-halved text-emerald-400"></i> توثيق الدخول الوطني (NAS)
            </span>
        </div>
        <div class="flex items-center gap-3">
            <span class="bg-qatar-maroonDeep px-2.5 py-0.5 rounded text-[11px] border border-qatar-gold/40 text-qatar-gold font-bold flex items-center gap-1">
                <i class="fa-solid fa-database"></i> مزامنة نظام مـوارد (SAP)
            </span>
            <span class="text-white/60">|</span>
            <button class="hover:text-qatar-gold font-semibold transition">English</button>
        </div>
    </div>

    <!-- 2. الترويسة الرئيسية والشعار الموحد (FutureX + طموح + مسارات التعلم المرن) -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- الشعار -->
                <div class="flex items-center gap-3.5 cursor-pointer" onclick="switchView('dashboard-view')">
                    <div class="w-12 h-12 maroon-gradient rounded-2xl flex items-center justify-center text-white shadow-md shadow-qatar-maroon/30 border border-qatar-gold/50">
                        <i class="fa-solid fa-graduation-cap text-2xl text-qatar-gold"></i>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="text-2xl font-black text-qatar-maroon tracking-tight">كَــفَــاءَة</span>
                            <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2 py-0.5 rounded-md border border-qatar-maroon/20">
                                المنظومة الوطنية الموحدة
                            </span>
                        </div>
                        <p class="text-[11px] text-slate-500 font-medium">التعلم المرن التراكمي • الربط مع Coursera ومـوارد</p>
                    </div>
                </div>

                <!-- شريط التنقل الشامل لكافة الخصائص المندمجة التراكمية -->
                <nav class="hidden xl:flex items-center gap-1">
                    <button onclick="switchView('dashboard-view')" id="nav-dashboard-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-bold text-qatar-maroon bg-qatar-maroonSoft border border-qatar-maroon/30 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-chart-line"></i> لوحتي وجواز المهارات
                    </button>
                    <button onclick="switchView('pathways-view')" id="nav-pathways-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-qatar-maroon hover:bg-qatar-maroonSoft/50 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-route text-qatar-maroon"></i> مسارات التعلم المرن
                    </button>
                    <button onclick="switchView('coursera-view')" id="nav-coursera-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-qatar-maroon hover:bg-qatar-maroonSoft/50 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-book-open"></i> مكتبة Coursera (16 مجالاً)
                    </button>
                    <button onclick="switchView('mentorship-view')" id="nav-mentorship-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-qatar-maroon hover:bg-qatar-maroonSoft/50 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-users-gear"></i> شبكة التوجيه
                    </button>
                    <button onclick="switchView('challenges-view')" id="nav-challenges-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-qatar-maroon hover:bg-qatar-maroonSoft/50 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-lightbulb"></i> التحديات الحكومية
                    </button>
                    <button onclick="switchView('entity-view')" id="nav-entity-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-qatar-maroon hover:bg-qatar-maroonSoft/50 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-building-user"></i> لوحة الجهات B2B
                    </button>
                    <button onclick="switchView('admin-excel-view')" id="nav-admin-excel-view" class="nav-btn px-2.5 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-qatar-maroon hover:bg-qatar-maroonSoft/50 flex items-center gap-1.5 transition">
                        <i class="fa-solid fa-file-excel text-emerald-600"></i> إدارة الإكسل والمواءمة
                    </button>
                </nav>

                <!-- ركن المستخدم ونقاط الجدارة التنافسية -->
                <div class="flex items-center gap-3">
                    <div class="flex items-center gap-2 bg-gradient-to-l from-amber-50 to-rose-50 border border-amber-200 px-3 py-1.5 rounded-xl shadow-xs">
                        <div class="w-7 h-7 gold-badge rounded-lg flex items-center justify-center text-qatar-maroonDark font-black text-xs shadow-xs">
                            <i class="fa-solid fa-award"></i>
                        </div>
                        <div class="text-right">
                            <div class="text-[9px] text-slate-500 font-bold">نقاط الجدارة</div>
                            <div class="text-xs font-black text-qatar-maroon" id="points-counter">3,450 نقطة</div>
                        </div>
                    </div>

                    <!-- الملف الشخصي -->
                    <div class="flex items-center gap-2.5 pr-2 border-r border-slate-200">
                        <div class="text-left hidden sm:block">
                            <div class="text-xs font-bold text-slate-800">م. ناصر الكعبي</div>
                            <div class="text-[10px] text-qatar-maroon font-semibold">مستشار رقمي - وزارة الاتصالات</div>
                        </div>
                        <div class="w-10 h-10 rounded-xl maroon-gradient text-white flex items-center justify-center font-bold text-sm ring-2 ring-qatar-maroon ring-offset-2 shadow-xs">
                            نك
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- شريط الهاتف المحمول المتجاوب -->
    <div class="xl:hidden bg-white border-b border-slate-200 px-4 py-2 flex overflow-x-auto gap-1.5 custom-scrollbar">
        <button onclick="switchView('dashboard-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-bold text-qatar-maroon bg-qatar-maroonSoft">لوحتي والمهارات</button>
        <button onclick="switchView('pathways-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 bg-slate-100">المسارات المرنة</button>
        <button onclick="switchView('coursera-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 bg-slate-100">مكتبة Coursera</button>
        <button onclick="switchView('mentorship-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 bg-slate-100">التوجيه</button>
        <button onclick="switchView('challenges-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 bg-slate-100">التحديات</button>
        <button onclick="switchView('entity-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 bg-slate-100">لوحة الجهة</button>
        <button onclick="switchView('admin-excel-view')" class="whitespace-nowrap px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 bg-slate-100">فحص الإكسل</button>
    </div>

    <!-- الحاوية التشغيلية الرئيسية -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

        <!-- ========================================================= -->
        <!-- الشاشة 1: لوحة المتدرب + جواز المهارات الرقمي + التلعيب     -->
        <!-- ========================================================= -->
        <section id="view-dashboard-view" class="space-y-6">
            <!-- لافتة الترحيب العنابية الوطنية -->
            <div class="maroon-card-gradient rounded-3xl p-6 sm:p-8 text-white relative overflow-hidden shadow-xl border border-qatar-maroonLight">
                <div class="absolute -left-12 -bottom-12 opacity-10 pointer-events-none">
                    <i class="fa-solid fa-award text-9xl"></i>
                </div>
                <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
                    <div class="max-w-2xl">
                        <div class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md px-3 py-1 rounded-full text-xs font-bold text-qatar-gold border border-white/15 mb-3">
                            <i class="fa-solid fa-crown"></i> المرتبة الأولى في كفاءات التحول الرقمي بالوزارة
                        </div>
                        <h1 class="text-2xl sm:text-3xl font-black mb-2">أهلاً بك في مسارات التعلم المرن، م. ناصر 👋</h1>
                        <p class="text-white/85 text-xs sm:text-sm leading-relaxed">
                            منصتك الموحدة تجمع بين مقررات Coursera المعتمدة، وتوجيه القيادات الحكومية، وحل التحديات الوطنية. يمكنك استكشاف المسارات المرنة والشجرية واختيار مستوى البدء بحرية.
                        </p>
                    </div>
                    <div class="flex flex-col sm:flex-row gap-3">
                        <button onclick="openModal('passport-modal')" class="bg-qatar-gold hover:bg-qatar-goldDark text-qatar-maroonDark font-black px-5 py-3 rounded-xl shadow-lg transition flex items-center justify-center gap-2 text-xs sm:text-sm">
                            <i class="fa-solid fa-passport text-base"></i>
                            <span>جواز المهارات الوطني</span>
                        </button>
                        <button onclick="switchView('pathways-view')" class="bg-white/15 hover:bg-white/25 text-white font-bold px-4 py-3 rounded-xl backdrop-blur-md border border-white/20 transition flex items-center justify-center gap-2 text-xs sm:text-sm">
                            <i class="fa-solid fa-route text-qatar-gold"></i>
                            <span>استكشاف المسارات الشجرية</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- بطاقات مؤشرات الأداء المتكاملة (FutureX + طموح) -->
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:border-qatar-maroon/50 transition">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-slate-500">ساعات التعلم المعتمدة</span>
                        <div class="w-8 h-8 rounded-lg bg-qatar-maroonSoft text-qatar-maroon flex items-center justify-center font-bold">
                            <i class="fa-solid fa-clock"></i>
                        </div>
                    </div>
                    <div class="text-2xl font-black text-slate-800">62.5 <span class="text-xs font-semibold text-slate-400">ساعة</span></div>
                    <div class="text-[11px] text-emerald-600 font-bold mt-1 flex items-center gap-1">
                        <i class="fa-solid fa-check-double"></i> متزامنة مع نظام مـوارد
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:border-qatar-maroon/50 transition">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-slate-500">الشهادات الصادرة</span>
                        <div class="w-8 h-8 rounded-lg bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
                            <i class="fa-solid fa-certificate"></i>
                        </div>
                    </div>
                    <div class="text-2xl font-black text-slate-800">6 <span class="text-xs font-semibold text-slate-400">شهادات</span></div>
                    <div class="text-[11px] text-qatar-maroon font-bold mt-1">
                        معتمدة من Coursera ومعهد الإدارة
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:border-qatar-maroon/50 transition">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-slate-500">جلسات الإرشاد والتوجيه</span>
                        <div class="w-8 h-8 rounded-lg bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
                            <i class="fa-solid fa-user-tie"></i>
                        </div>
                    </div>
                    <div class="text-2xl font-black text-slate-800">4 <span class="text-xs font-semibold text-slate-400">جلسات</span></div>
                    <div class="text-[11px] text-purple-600 font-bold mt-1">
                        مع وكلاء وزارة وخبراء دوليين
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-xs hover:border-qatar-maroon/50 transition">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-slate-500">المشاريع والتحديات</span>
                        <div class="w-8 h-8 rounded-lg bg-rose-50 text-qatar-maroon flex items-center justify-center font-bold">
                            <i class="fa-solid fa-diagram-project"></i>
                        </div>
                    </div>
                    <div class="text-2xl font-black text-slate-800">2 <span class="text-xs font-semibold text-slate-400">مشروعان</span></div>
                    <div class="text-[11px] text-emerald-600 font-bold mt-1">
                        حلول مقدمة لوزارة الصحة
                    </div>
                </div>
            </div>

            <!-- شبكة البرامج الجارية ولوحة الصدارة ومحرك التوصيات -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- المقررات الجارية (Coursera) -->
                <div class="lg:col-span-2 space-y-4">
                    <div class="flex justify-between items-center">
                        <h2 class="text-base font-black text-slate-800 flex items-center gap-2">
                            <i class="fa-solid fa-play-circle text-qatar-maroon"></i>
                            البرامج والمسارات الجارية عبر Coursera SSO
                        </h2>
                        <button onclick="switchView('coursera-view')" class="text-xs font-bold text-qatar-maroon hover:underline">
                            المكتبة الشاملة &larr;
                        </button>
                    </div>

                    <!-- مقرر قيد الإنجاز 1 -->
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hover:border-qatar-maroon/40 transition">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-3">
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2 py-0.5 rounded border border-qatar-maroon/20">Coursera API</span>
                                    <span class="text-xs font-bold text-slate-500">Stanford Online</span>
                                </div>
                                <h3 class="text-sm font-black text-slate-800">الذكاء الاصطناعي التوليدي والسياسات العامة (GenAI Governance)</h3>
                            </div>
                            <span class="text-xs font-bold text-qatar-maroon bg-qatar-maroonSoft px-3 py-1 rounded-full border border-qatar-maroon/20 self-start sm:self-auto">
                                75% مكتمل
                            </span>
                        </div>
                        <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden mb-4">
                            <div class="bg-qatar-maroon h-full rounded-full transition-all duration-500" style="width: 75%"></div>
                        </div>
                        <div class="flex items-center justify-between pt-3 border-t border-slate-100 text-xs">
                            <span class="text-slate-500"><i class="fa-regular fa-clock ml-1"></i> متبقي ساعتان لإتمام المستوى المتقدم</span>
                            <button onclick="showToast('جاري فتح جلسة التعلم عبر Coursera SSO...')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white font-bold px-4 py-2 rounded-lg transition shadow-xs flex items-center gap-1.5">
                                <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i> استئناف التعلم
                            </button>
                        </div>
                    </div>

                    <!-- مقرر قيد الإنجاز 2 -->
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hover:border-qatar-maroon/40 transition">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-3">
                            <div>
                                <div class="flex items-center gap-2 mb-1">
                                    <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2 py-0.5 rounded border border-qatar-maroon/20">Coursera API</span>
                                    <span class="text-xs font-bold text-slate-500">London Business School</span>
                                </div>
                                <h3 class="text-sm font-black text-slate-800">التفكير الاستراتيجي وصناعة السيناريوهات المستقبلية</h3>
                            </div>
                            <span class="text-xs font-bold text-amber-700 bg-amber-50 px-3 py-1 rounded-full border border-amber-200 self-start sm:self-auto">
                                40% مكتمل
                            </span>
                        </div>
                        <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden mb-4">
                            <div class="bg-qatar-maroon h-full rounded-full transition-all duration-500" style="width: 40%"></div>
                        </div>
                        <div class="flex items-center justify-between pt-3 border-t border-slate-100 text-xs">
                            <span class="text-slate-500"><i class="fa-regular fa-clock ml-1"></i> موعد الاختبار التفاعلي: الأحد القادم</span>
                            <button onclick="showToast('جاري فتح جلسة التعلم عبر Coursera SSO...')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white font-bold px-4 py-2 rounded-lg transition shadow-xs flex items-center gap-1.5">
                                <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i> استئناف التعلم
                            </button>
                        </div>
                    </div>
                </div>

                <!-- لوحة الصدارة ومحرك التوصيات الذكي الثلاثي -->
                <div class="space-y-4">
                    <!-- محرك التوصيات الذكي الثلاثي المطور -->
                    <div class="maroon-card-gradient text-white p-5 rounded-2xl shadow-sm border border-qatar-maroonLight">
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2 text-qatar-gold text-xs font-bold">
                                <i class="fa-solid fa-wand-magic-sparkles"></i> محرك التوصيات الذكي (AI)
                            </div>
                            <span class="bg-white/10 px-2 py-0.5 rounded text-[10px] text-white/90">مربوط بمـوارد</span>
                        </div>
                        <div class="text-[11px] text-white/80 mb-3">بناءً على مسماك الوظيفي وتقييم الجدارات بديوان الخدمة:</div>
                        
                        <!-- توصية 1: مرتبطة بالوظيفة الحالية -->
                        <div class="bg-white/10 p-3 rounded-xl mb-2 border border-white/10">
                            <div class="text-[10px] font-bold text-qatar-gold mb-0.5"><i class="fa-solid fa-briefcase"></i> 1. مرتبطة بوظيفتك الحالية:</div>
                            <div class="text-xs font-black">حوكمة وإدارة البيانات الحكومية الضخمة</div>
                            <div class="text-[10px] text-white/70 mt-1">سد فجوة: الكفاءة الفنية للتحول الرقمي</div>
                        </div>

                        <!-- توصية 2: تطوير المهارات -->
                        <div class="bg-white/10 p-3 rounded-xl mb-3 border border-white/10">
                            <div class="text-[10px] font-bold text-emerald-300 mb-0.5"><i class="fa-solid fa-arrow-trend-up"></i> 2. لتطوير مهاراتك:</div>
                            <div class="text-xs font-black">الذكاء الاصطناعي التوليدي للمديرين التنفيذيين</div>
                            <div class="text-[10px] text-white/70 mt-1">تطوير: كفاءة الابتكار وصناعة القرار</div>
                        </div>

                        <button onclick="enrollCourse('حوكمة البيانات الحكومية الضخمة')" class="w-full bg-white text-qatar-maroon hover:bg-qatar-maroonSoft text-xs font-bold py-2 rounded-lg transition shadow-xs">
                            إضافة للخطة الفردية (IDP) +
                        </button>
                    </div>

                    <!-- لوحة التنافس ولوحة الصدارة (طموح) -->
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                        <div class="flex items-center justify-between mb-3 pb-2 border-b border-slate-100">
                            <h3 class="font-black text-xs text-slate-800 flex items-center gap-2">
                                <i class="fa-solid fa-ranking-star text-qatar-gold"></i>
                                لوحة صدارة الكفاءات (الجهات الحكومية)
                            </h3>
                            <span class="text-[10px] font-bold text-qatar-maroon bg-qatar-maroonSoft px-2 py-0.5 rounded">دولة قطر</span>
                        </div>
                        <div class="space-y-2">
                            <div class="flex items-center justify-between p-2 rounded-xl bg-amber-50/70 border border-amber-200/60">
                                <div class="flex items-center gap-2">
                                    <span class="w-5 h-5 rounded-full bg-amber-500 text-white font-black text-[10px] flex items-center justify-center">1</span>
                                    <span class="text-xs font-bold text-slate-800">مها السليطي (وزارة العدل)</span>
                                </div>
                                <span class="text-xs font-black text-qatar-maroon">3,890 ن</span>
                            </div>
                            <div class="flex items-center justify-between p-2 rounded-xl bg-qatar-maroonSoft border border-qatar-maroon/30 shadow-xs">
                                <div class="flex items-center gap-2">
                                    <span class="w-5 h-5 rounded-full bg-qatar-maroon text-white font-black text-[10px] flex items-center justify-center">3</span>
                                    <span class="text-xs font-black text-qatar-maroon">أنت (م. ناصر الكعبي)</span>
                                </div>
                                <span class="text-xs font-black text-qatar-maroon">3,450 ن</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- الشاشة 2: منظومة مسارات التعلم المرن الشجرية (الهيكل التفرعي) -->
        <!-- ========================================================= -->
        <section id="view-pathways-view" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                    <div>
                        <div class="inline-flex items-center gap-1.5 bg-qatar-maroonSoft text-qatar-maroon text-xs font-bold px-3 py-1 rounded-full mb-2 border border-qatar-maroon/20">
                            <i class="fa-solid fa-sitemap"></i> هيكل المسارات الشجرية التفرعية (Tree Structure)
                        </div>
                        <h2 class="text-xl font-black text-slate-800">منظومة مسارات التعلم المرن التخصصية</h2>
                        <p class="text-xs text-slate-500 mt-1">
                            مسارات رئيسية تتفرع إلى مسارات فرعية دقيقة عبر 4 مستويات: التأسيسي، التطبيقي، المتقدم، والاحترافي. حرية تامة في اختيار المستوى والمسار دون قيود إلزامية.
                        </p>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="openModal('journey-modal')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-4 py-2.5 rounded-xl transition shadow-xs flex items-center gap-2">
                            <i class="fa-solid fa-map-location-dot"></i> خريطة الرحلة التعليمية
                        </button>
                    </div>
                </div>

                <!-- تصفية الأقسام الستة للمسارات -->
                <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-100">
                    <button onclick="filterPathwayType('ALL')" class="pathway-filter-btn active bg-qatar-maroon text-white text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-all">جميع المسارات</button>
                    <button onclick="filterPathwayType('COMMON')" class="pathway-filter-btn bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-common">1. المسارات المشتركة</button>
                    <button onclick="filterPathwayType('JOB')" class="pathway-filter-btn bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-job">2. المسارات الوظيفية</button>
                    <button onclick="filterPathwayType('SPEC')" class="pathway-filter-btn bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-spec">3. المسارات التخصصية</button>
                    <button onclick="filterPathwayType('LEAD')" class="pathway-filter-btn bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-lead">4. المسارات القيادية المتدرجة</button>
                    <button onclick="filterPathwayType('FUTURE')" class="pathway-filter-btn bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-future">5. مهارات المستقبل</button>
                    <button onclick="filterPathwayType('PERSONAL')" class="pathway-filter-btn bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-3.5 py-1.5 rounded-lg transition" id="p-btn-personal">6. مساراتي الشخصية</button>
                </div>
            </div>

            <!-- عرض المسارات الشجرية المتقدمة -->
            <div class="space-y-6" id="pathways-container">
                <!-- المسار الرئيسي 1: الذكاء الاصطناعي -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden pathway-block" data-type="COMMON SPEC FUTURE">
                    <div class="p-6 bg-gradient-to-r from-slate-50 to-white border-b border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="flex items-center gap-3">
                            <div class="w-12 h-12 rounded-xl maroon-gradient text-white flex items-center justify-center text-xl shadow-xs">
                                <i class="fa-solid fa-brain text-qatar-gold"></i>
                            </div>
                            <div>
                                <div class="flex items-center gap-2">
                                    <h3 class="text-base font-black text-slate-800">المسار الرئيسي: الذكاء الاصطناعي (Artificial Intelligence)</h3>
                                    <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2 py-0.5 rounded border border-qatar-maroon/20">6 مسارات فرعية</span>
                                </div>
                                <p class="text-xs text-slate-500 mt-0.5">الكفاءات المستهدفة: التحول الرقمي، الابتكار المؤسسي، حوكمة الخوارزميات، وصناعة القرار المرتكز على البيانات</p>
                            </div>
                        </div>
                        <span class="text-xs font-bold text-slate-600 bg-white px-3 py-1.5 rounded-xl border border-slate-200 self-start md:self-auto">
                            مستويات مرنة (تأسيسي &larr; احترافي)
                        </span>
                    </div>

                    <!-- شبكة المسارات الفرعية المتفرعة عنه -->
                    <div class="p-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        <!-- فرع 1 -->
                        <div class="p-4 rounded-xl border border-slate-200 hover:border-qatar-maroon transition bg-slate-50/50 flex flex-col justify-between">
                            <div>
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">المستوى 1: التأسيسي</span>
                                    <span class="text-xs text-slate-400">12 ساعة</span>
                                </div>
                                <h4 class="font-black text-sm text-slate-800 mb-1">الذكاء الاصطناعي للمبتدئين</h4>
                                <p class="text-xs text-slate-500 mb-3">مفاهيم الذكاء الاصطناعي والتعلم الآلي الأساسية وأخلاقيات الاستخدام في بيئة العمل.</p>
                                <div class="text-[11px] font-semibold text-slate-600"><i class="fa-solid fa-book text-qatar-maroon ml-1"></i> 3 برامج معتمدة من IBM & DeepLearning.AI</div>
                            </div>
                            <div class="mt-4 pt-3 border-t border-slate-200 flex justify-between items-center">
                                <button onclick="openJourneyMap('الذكاء الاصطناعي للمبتدئين', 'تأسيسي')" class="text-xs font-bold text-qatar-maroon hover:underline">عرض الخريطة</button>
                                <button onclick="enrollCourse('الذكاء الاصطناعي للمبتدئين')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3 py-1.5 rounded-lg transition">بدء المسار</button>
                            </div>
                        </div>

                        <!-- فرع 2 -->
                        <div class="p-4 rounded-xl border border-slate-200 hover:border-qatar-maroon transition bg-slate-50/50 flex flex-col justify-between">
                            <div>
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-[10px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded">المستوى 2: التطبيقي</span>
                                    <span class="text-xs text-slate-400">18 ساعة</span>
                                </div>
                                <h4 class="font-black text-sm text-slate-800 mb-1">الذكاء الاصطناعي للموظف الحكومي</h4>
                                <p class="text-xs text-slate-500 mb-3">توظيف أدوات الأتمتة وصياغة الأوامر (Prompt Engineering) لرفع الإنتاجية اليومية.</p>
                                <div class="text-[11px] font-semibold text-slate-600"><i class="fa-solid fa-book text-qatar-maroon ml-1"></i> 4 برامج معتمدة من Vanderbilt University</div>
                            </div>
                            <div class="mt-4 pt-3 border-t border-slate-200 flex justify-between items-center">
                                <button onclick="openJourneyMap('الذكاء الاصطناعي للموظف الحكومي', 'تطبيقي')" class="text-xs font-bold text-qatar-maroon hover:underline">عرض الخريطة</button>
                                <button onclick="enrollCourse('الذكاء الاصطناعي للموظف الحكومي')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3 py-1.5 rounded-lg transition">بدء المسار</button>
                            </div>
                        </div>

                        <!-- فرع 3 -->
                        <div class="p-4 rounded-xl border-2 border-qatar-maroon bg-qatar-maroonSoft/30 flex flex-col justify-between relative">
                            <span class="absolute -top-2.5 right-3 bg-qatar-maroon text-white text-[9px] font-black px-2 py-0.5 rounded-full">الأكثر إقبالاً</span>
                            <div>
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-[10px] font-bold text-purple-700 bg-purple-50 px-2 py-0.5 rounded">المستوى 3: المتقدم</span>
                                    <span class="text-xs text-slate-400">26 ساعة</span>
                                </div>
                                <h4 class="font-black text-sm text-slate-800 mb-1">الذكاء الاصطناعي للمديرين وصنّاع القرار</h4>
                                <p class="text-xs text-slate-500 mb-3">إدارة استراتيجيات التحول الذكي، تقييم العائد الاستثماري، وضمان أمن وسرية البيانات الحكومية.</p>
                                <div class="text-[11px] font-semibold text-slate-600"><i class="fa-solid fa-book text-qatar-maroon ml-1"></i> 5 برامج معتمدة من Stanford & Wharton</div>
                            </div>
                            <div class="mt-4 pt-3 border-t border-qatar-maroon/20 flex justify-between items-center">
                                <button onclick="openJourneyMap('الذكاء الاصطناعي للمديرين', 'متقدم')" class="text-xs font-bold text-qatar-maroon hover:underline">عرض الخريطة</button>
                                <button onclick="enrollCourse('الذكاء الاصطناعي للمديرين وصناع القرار')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3 py-1.5 rounded-lg transition">بدء المسار</button>
                            </div>
                        </div>

                        <!-- فرع 4 -->
                        <div class="p-4 rounded-xl border border-slate-200 hover:border-qatar-maroon transition bg-slate-50/50 flex flex-col justify-between">
                            <div>
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-[10px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded">المستوى 2: التطبيقي</span>
                                    <span class="text-xs text-slate-400">22 ساعة</span>
                                </div>
                                <h4 class="font-black text-sm text-slate-800 mb-1">الذكاء الاصطناعي لتحليل البيانات</h4>
                                <p class="text-xs text-slate-500 mb-3">ربط تقنيات النمذجة التنبؤية بالبيانات التشغيلية في الجهات الحكومية واستخراج الرؤى.</p>
                                <div class="text-[11px] font-semibold text-slate-600"><i class="fa-solid fa-book text-qatar-maroon ml-1"></i> 4 برامج معتمدة من Google Cloud</div>
                            </div>
                            <div class="mt-4 pt-3 border-t border-slate-200 flex justify-between items-center">
                                <button onclick="openJourneyMap('الذكاء الاصطناعي لتحليل البيانات', 'تطبيقي')" class="text-xs font-bold text-qatar-maroon hover:underline">عرض الخريطة</button>
                                <button onclick="enrollCourse('الذكاء الاصطناعي لتحليل البيانات')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3 py-1.5 rounded-lg transition">بدء المسار</button>
                            </div>
                        </div>

                        <!-- فرع 5 -->
                        <div class="p-4 rounded-xl border border-slate-200 hover:border-qatar-maroon transition bg-slate-50/50 flex flex-col justify-between">
                            <div>
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-[10px] font-bold text-purple-700 bg-purple-50 px-2 py-0.5 rounded">المستوى 3: المتقدم</span>
                                    <span class="text-xs text-slate-400">20 ساعة</span>
                                </div>
                                <h4 class="font-black text-sm text-slate-800 mb-1">الذكاء الاصطناعي التوليدي (GenAI)</h4>
                                <p class="text-xs text-slate-500 mb-3">بناء وتخصيص نماذج اللغة الضخمة وتطبيقاتها في أتمتة الوثائق والخدمات الذكية.</p>
                                <div class="text-[11px] font-semibold text-slate-600"><i class="fa-solid fa-book text-qatar-maroon ml-1"></i> 4 برامج معتمدة من AWS & DeepLearning</div>
                            </div>
                            <div class="mt-4 pt-3 border-t border-slate-200 flex justify-between items-center">
                                <button onclick="openJourneyMap('الذكاء الاصطناعي التوليدي', 'متقدم')" class="text-xs font-bold text-qatar-maroon hover:underline">عرض الخريطة</button>
                                <button onclick="enrollCourse('الذكاء الاصطناعي التوليدي')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3 py-1.5 rounded-lg transition">بدء المسار</button>
                            </div>
                        </div>

                        <!-- فرع 6 -->
                        <div class="p-4 rounded-xl border border-slate-200 hover:border-qatar-maroon transition bg-slate-50/50 flex flex-col justify-between">
                            <div>
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-[10px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded">المستوى 4: الاحترافي</span>
                                    <span class="text-xs text-slate-400">35 ساعة + مشروع</span>
                                </div>
                                <h4 class="font-black text-sm text-slate-800 mb-1">تطبيقات الذكاء الاصطناعي المتقدمة وحوكمة النظم</h4>
                                <p class="text-xs text-slate-500 mb-3">هندسة الحلول السيادية والامتثال لأطر أمن وحماية البيانات الوطنية لدولة قطر.</p>
                                <div class="text-[11px] font-semibold text-slate-600"><i class="fa-solid fa-book text-qatar-maroon ml-1"></i> 6 برامج معتمدة من MIT & IBM</div>
                            </div>
                            <div class="mt-4 pt-3 border-t border-slate-200 flex justify-between items-center">
                                <button onclick="openJourneyMap('تطبيقات الذكاء الاصطناعي المتقدمة', 'احترافي')" class="text-xs font-bold text-qatar-maroon hover:underline">عرض الخريطة</button>
                                <button onclick="enrollCourse('تطبيقات الذكاء الاصطناعي المتقدمة')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3 py-1.5 rounded-lg transition">بدء المسار</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- المسار الرئيسي 2: المسارات القيادية المتدرجة بحسب المستوى الإداري -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden pathway-block" data-type="LEAD">
                    <div class="p-6 bg-gradient-to-r from-slate-50 to-white border-b border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="flex items-center gap-3">
                            <div class="w-12 h-12 rounded-xl maroon-gradient text-white flex items-center justify-center text-xl shadow-xs">
                                <i class="fa-solid fa-user-tie text-qatar-gold"></i>
                            </div>
                            <div>
                                <div class="flex items-center gap-2">
                                    <h3 class="text-base font-black text-slate-800">المسارات القيادية الحكومية المتدرجة</h3>
                                    <span class="bg-purple-100 text-purple-800 text-[10px] font-bold px-2 py-0.5 rounded">مبنية على الهيكل الإداري</span>
                                </div>
                                <p class="text-xs text-slate-500 mt-0.5">مسارات مصممة خصيصاً للتدرج من الموظف الواعد وصولاً إلى القيادات التنفيذية العليا</p>
                            </div>
                        </div>
                    </div>

                    <div class="p-6 grid grid-cols-1 md:grid-cols-5 gap-3">
                        <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50 text-center">
                            <div class="text-[10px] font-bold text-slate-500 mb-1">المحطة 1</div>
                            <div class="font-black text-xs text-slate-800 mb-1">إعداد الموظفين للقيادة</div>
                            <span class="text-[10px] text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded font-bold">المستوى التأسيسي</span>
                        </div>
                        <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50 text-center">
                            <div class="text-[10px] font-bold text-slate-500 mb-1">المحطة 2</div>
                            <div class="font-black text-xs text-slate-800 mb-1">المهارات الإشرافية</div>
                            <span class="text-[10px] text-blue-700 bg-blue-50 px-2 py-0.5 rounded font-bold">المستوى التطبيقي</span>
                        </div>
                        <div class="p-3.5 rounded-xl border-2 border-qatar-maroon bg-qatar-maroonSoft/40 text-center">
                            <div class="text-[10px] font-bold text-qatar-maroon mb-1">المحطة 3 (الحالية)</div>
                            <div class="font-black text-xs text-slate-800 mb-1">رؤساء الأقسام</div>
                            <span class="text-[10px] text-purple-700 bg-purple-50 px-2 py-0.5 rounded font-bold">المستوى المتقدم</span>
                        </div>
                        <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50 text-center opacity-85">
                            <div class="text-[10px] font-bold text-slate-500 mb-1">المحطة 4</div>
                            <div class="font-black text-xs text-slate-800 mb-1">مدراء الإدارات</div>
                            <span class="text-[10px] text-rose-700 bg-rose-50 px-2 py-0.5 rounded font-bold">المستوى الاحترافي</span>
                        </div>
                        <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50 text-center opacity-85">
                            <div class="text-[10px] font-bold text-slate-500 mb-1">المحطة 5</div>
                            <div class="font-black text-xs text-slate-800 mb-1">القيادات التنفيذية</div>
                            <span class="text-[10px] text-amber-700 bg-amber-50 px-2 py-0.5 rounded font-bold">استراتيجي سيادي</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- الشاشة 3: مكتبة Coursera (16 مجالات - مستوحاة من FutureX) -->
        <!-- ========================================================= -->
        <section id="view-coursera-view" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="bg-qatar-maroon text-white text-[10px] font-bold px-2 py-0.5 rounded">Coursera Catalog API</span>
                            <span class="text-xs font-bold text-emerald-600 flex items-center gap-1">
                                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> متزامن بالكامل مع سحابة معهد الإدارة العامة
                            </span>
                        </div>
                        <h2 class="text-xl font-black text-slate-800">مكتبة البرامج والشهادات المهنية المعتمدة</h2>
                        <p class="text-xs text-slate-500 mt-1">تصفح البرامج المصنفة حسب مجالات الكفاءة الوطنية الـ 16 بدولة قطر والمستوردة من الكتالوج الرسمي</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="text-right">
                            <span class="text-[10px] text-slate-400 font-bold block">رخص الجهة المتاحة</span>
                            <span class="text-sm font-black text-qatar-maroon">420 رخصة نشطة</span>
                        </div>
                    </div>
                </div>

                <!-- أدوات التصفية والبحث الفوري -->
                <div class="grid grid-cols-1 md:grid-cols-4 gap-3">
                    <div class="md:col-span-2 relative">
                        <i class="fa-solid fa-magnifying-glass absolute right-3.5 top-3.5 text-slate-400"></i>
                        <input type="text" id="course-search-input" onkeyup="filterCourses()" placeholder="ابحث باسم البرنامج، الجامعة المانحة، أو الكفاءة المستهدفة..." class="w-full pr-10 pl-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:border-qatar-maroon focus:bg-white transition">
                    </div>
                    <div>
                        <select id="course-category-select" onchange="filterCourses()" class="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:border-qatar-maroon text-slate-700 font-semibold">
                            <option value="ALL">جميع المجالات (16 مجالاً)</option>
                            <option value="AI">1. الذكاء الاصطناعي</option>
                            <option value="DIGITAL">2. التحول الرقمي</option>
                            <option value="DATA">3. تحليل البيانات</option>
                            <option value="CYBER">4. الأمن السيبراني</option>
                            <option value="LEADERSHIP">5. القيادة والإدارة</option>
                            <option value="STRATEGY">6. الإدارة الاستراتيجية</option>
                            <option value="PROJECTS">7. إدارة المشاريع</option>
                            <option value="INNOVATION">8. الابتكار والتفكير الإبداعي</option>
                            <option value="FUTURE">9. المهارات المستقبلية</option>
                        </select>
                    </div>
                    <div>
                        <select id="course-level-select" onchange="filterCourses()" class="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:border-qatar-maroon text-slate-700 font-semibold">
                            <option value="ALL">جميع المستويات الأربعة</option>
                            <option value="تأسيسي">المستوى الأول: التأسيسي</option>
                            <option value="تطبيقي">المستوى الثاني: التطبيقي</option>
                            <option value="متقدم">المستوى الثالث: المتقدم</option>
                            <option value="احترافي">المستوى الرابع: الاحترافي</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- شبكة الكروت التدريبية التفاعلية -->
            <div id="courses-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                <!-- كارت 1 -->
                <div class="course-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-lg hover:border-qatar-maroon/50 transition flex flex-col justify-between" data-category="AI" data-level="متقدم">
                    <div class="p-5">
                        <div class="flex justify-between items-start mb-3">
                            <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2.5 py-1 rounded-md border border-qatar-maroon/20">الذكاء الاصطناعي</span>
                            <span class="text-xs font-bold text-slate-400"><i class="fa-regular fa-clock ml-1"></i> 24 ساعة</span>
                        </div>
                        <h3 class="text-sm font-black text-slate-800 mb-2">استراتيجيات الذكاء الاصطناعي التوليدي للقطاع العام</h3>
                        <p class="text-xs text-slate-500 mb-3 leading-relaxed">بناء خارطة طريق لتطبيق نماذج الذكاء الاصطناعي في أتمتة الخدمات الحكومية مع ضمان الامتثال للأمن السيبراني.</p>
                        <div class="text-xs font-bold text-slate-600 mb-1 flex items-center gap-1.5">
                            <i class="fa-solid fa-building-columns text-qatar-maroon"></i> Vanderbilt University
                        </div>
                        <div class="text-xs text-emerald-600 font-semibold">
                            <i class="fa-solid fa-language"></i> متاح باللغة العربية والإنجليزية
                        </div>
                    </div>
                    <div class="p-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-qatar-maroon bg-white px-2 py-0.5 rounded border border-slate-200">المستوى: المتقدم</span>
                        <button onclick="enrollCourse('استراتيجيات الذكاء الاصطناعي للقطاع العام')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-4 py-2 rounded-lg transition shadow-xs">
                            التحاق مباشر
                        </button>
                    </div>
                </div>

                <!-- كارت 2 -->
                <div class="course-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-lg hover:border-qatar-maroon/50 transition flex flex-col justify-between" data-category="STRATEGY" data-level="تطبيقي">
                    <div class="p-5">
                        <div class="flex justify-between items-start mb-3">
                            <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2.5 py-1 rounded-md border border-qatar-maroon/20">الإدارة الاستراتيجية</span>
                            <span class="text-xs font-bold text-slate-400"><i class="fa-regular fa-clock ml-1"></i> 18 ساعة</span>
                        </div>
                        <h3 class="text-sm font-black text-slate-800 mb-2">التخطيط الاستراتيجي ومؤشرات الأداء KPI الحكومية</h3>
                        <p class="text-xs text-slate-500 mb-3 leading-relaxed">منهجيات مواءمة الخطط المؤسسية مع استراتيجية التنمية الوطنية الثالثة لدولة قطر (2024 - 2030).</p>
                        <div class="text-xs font-bold text-slate-600 mb-1 flex items-center gap-1.5">
                            <i class="fa-solid fa-building-columns text-qatar-maroon"></i> HEC Paris in Qatar
                        </div>
                        <div class="text-xs text-emerald-600 font-semibold">
                            <i class="fa-solid fa-language"></i> ترجمة احترافية معتمدة
                        </div>
                    </div>
                    <div class="p-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 bg-white px-2 py-0.5 rounded border border-slate-200">المستوى: التطبيقي</span>
                        <button onclick="enrollCourse('التخطيط الاستراتيجي ومؤشرات KPI')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-4 py-2 rounded-lg transition shadow-xs">
                            التحاق مباشر
                        </button>
                    </div>
                </div>

                <!-- كارت 3 -->
                <div class="course-card bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-lg hover:border-qatar-maroon/50 transition flex flex-col justify-between" data-category="CYBER" data-level="احترافي">
                    <div class="p-5">
                        <div class="flex justify-between items-start mb-3">
                            <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2.5 py-1 rounded-md border border-qatar-maroon/20">الأمن السيبراني</span>
                            <span class="text-xs font-bold text-slate-400"><i class="fa-regular fa-clock ml-1"></i> 32 ساعة</span>
                        </div>
                        <h3 class="text-sm font-black text-slate-800 mb-2">إدارة حوادث الأمن السيبراني وحماية البنى الحيوية</h3>
                        <p class="text-xs text-slate-500 mb-3 leading-relaxed">متوافق مع أطر الوكالة الوطنية للأمن السيبراني في دولة قطر لحماية البيانات والأنظمة الحكومية.</p>
                        <div class="text-xs font-bold text-slate-600 mb-1 flex items-center gap-1.5">
                            <i class="fa-brands fa-ibm text-qatar-maroon"></i> IBM Security
                        </div>
                        <div class="text-xs text-emerald-600 font-semibold">
                            <i class="fa-solid fa-language"></i> باللغة العربية والإنجليزية
                        </div>
                    </div>
                    <div class="p-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-rose-700 bg-white px-2 py-0.5 rounded border border-slate-200">المستوى: الاحترافي</span>
                        <button onclick="enrollCourse('إدارة حوادث الأمن السيبراني')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-4 py-2 rounded-lg transition shadow-xs">
                            التحاق مباشر
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- الشاشة 4: شبكة التوجيه والإرشاد المهني (مستوحاة من طموح)     -->
        <!-- ========================================================= -->
        <section id="view-mentorship-view" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <div class="inline-flex items-center gap-1.5 bg-purple-50 text-purple-800 text-xs font-bold px-3 py-1 rounded-full mb-2">
                            <i class="fa-solid fa-handshake-angle"></i> منصة نقل الخبرات والتوجيه الحكومي
                        </div>
                        <h2 class="text-xl font-black text-slate-800">شبكة المرشدين والقيادات الوطنية المعتمدة</h2>
                        <p class="text-xs text-slate-500 mt-1">احجز جلسات توجيه مهني فردية (1-on-1) مع وكلاء الوزارات والخبراء المعتمدين لتسريع مسارك المهني</p>
                    </div>
                    <button onclick="showToast('جاري فتح معايير الانضمام كمرشد معتمد...')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-4 py-2.5 rounded-xl transition flex items-center gap-2">
                        <i class="fa-solid fa-id-badge text-qatar-maroon"></i> الانضمام كمرشد معتمد
                    </button>
                </div>
            </div>

            <!-- بطاقات المرشدين والخبراء -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md hover:border-qatar-maroon/40 transition">
                    <div class="flex items-center gap-3.5 mb-4">
                        <div class="w-14 h-14 rounded-2xl maroon-gradient text-white flex items-center justify-center text-lg font-black border-2 border-qatar-gold/50 shadow-xs">
                            س.ك
                        </div>
                        <div>
                            <h3 class="font-black text-sm text-slate-800">سعادة د. حمد الكواري</h3>
                            <p class="text-xs text-qatar-maroon font-bold">خبير التخطيط الاستراتيجي والحوكمة</p>
                            <span class="text-[10px] text-slate-400">خبرة +22 عاماً بالقطاع الحكومي</span>
                        </div>
                    </div>
                    <div class="text-xs text-slate-600 bg-slate-50 p-3 rounded-xl mb-4 leading-relaxed">
                        مجالات التوجيه: صناعة القرارات الاستراتيجية، قيادة فرق التحول الكبرى، وتطوير القيادات الشابة.
                    </div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                        <span class="text-xs text-emerald-600 font-bold"><i class="fa-regular fa-calendar-check ml-1"></i> متاح هذا الأسبوع</span>
                        <button onclick="bookMentorship('سعادة د. حمد الكواري')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3.5 py-2 rounded-lg transition shadow-xs">
                            حجز جلسة توجيه
                        </button>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md hover:border-qatar-maroon/40 transition">
                    <div class="flex items-center gap-3.5 mb-4">
                        <div class="w-14 h-14 rounded-2xl maroon-gradient text-white flex items-center justify-center text-lg font-black border-2 border-qatar-gold/50 shadow-xs">
                            ع.م
                        </div>
                        <div>
                            <h3 class="font-black text-sm text-slate-800">م. عائشة المحمود</h3>
                            <p class="text-xs text-qatar-maroon font-bold">مدير التحول الرقمي والذكاء الاصطناعي</p>
                            <span class="text-[10px] text-slate-400">مستشار رقمي معتمد لدى ديوان الخدمة</span>
                        </div>
                    </div>
                    <div class="text-xs text-slate-600 bg-slate-50 p-3 rounded-xl mb-4 leading-relaxed">
                        مجالات التوجيه: قيادة مشاريع الذكاء الاصطناعي، إدارة التغيير التقني، وتطوير المواهب الرقمية.
                    </div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                        <span class="text-xs text-emerald-600 font-bold"><i class="fa-regular fa-calendar-check ml-1"></i> متاح يوم الخميس</span>
                        <button onclick="bookMentorship('م. عائشة المحمود')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white text-xs font-bold px-3.5 py-2 rounded-lg transition shadow-xs">
                            حجز جلسة توجيه
                        </button>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md hover:border-qatar-maroon/40 transition">
                    <div class="flex items-center gap-3.5 mb-4">
                        <div class="w-14 h-14 rounded-2xl maroon-gradient text-white flex items-center justify-center text-lg font-black border-2 border-qatar-gold/50 shadow-xs">
                            ف.س
                        </div>
                        <div>
                            <h3 class="font-black text-sm text-slate-800">أ. فهد السليطي</h3>
                            <p class="text-xs text-qatar-maroon font-bold">خبير الموارد البشرية والابتكار المؤسسي</p>
                            <span class="text-[10px] text-slate-400">عضو لجنة الكفاءات الحكومية</span>
                        </div>
                    </div>
                    <div class="text-xs text-slate-600 bg-slate-50 p-3 rounded-xl mb-4 leading-relaxed">
                        مجالات التوجيه: مصفوفة الجدارات الوظيفية، صياغة خطط التطوير الفردية، وتجاوز العقبات القيادية.
                    </div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-100">
                        <span class="text-xs text-slate-400 font-bold"><i class="fa-regular fa-clock ml-1"></i> الجلسات القادمة مكتملة</span>
                        <button onclick="showToast('تمت إضافتك لقائمة الانتظار لهذا المرشد')" class="bg-slate-200 hover:bg-slate-300 text-slate-700 text-xs font-bold px-3.5 py-2 rounded-lg transition">
                            قائمة الانتظار
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- الشاشة 5: التحديات والمشاريع الحكومية التطبيقية (طموح)       -->
        <!-- ========================================================= -->
        <section id="view-challenges-view" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <div class="inline-flex items-center gap-1.5 bg-rose-50 text-qatar-maroon text-xs font-bold px-3 py-1 rounded-full mb-2 border border-qatar-maroon/20">
                            <i class="fa-solid fa-lightbulb"></i> ربط المعرفة بالتطبيق العملي الوطني
                        </div>
                        <h2 class="text-xl font-black text-slate-800">مختبر التحديات والمشاريع الحكومية الوطنية</h2>
                        <p class="text-xs text-slate-500 mt-1">تحديات حقيقية مطروحة من الوزارات القطرية. حلولك المبتكرة تؤهلك للحصول على اعتمادات واحتساب ساعات إضافية بنظام موارد</p>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold text-slate-600">التحديات النشطة: <strong>14 تحدياً</strong></span>
                    </div>
                </div>
            </div>

            <!-- بطاقات التحديات المطروحة -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs hover:border-qatar-maroon/50 transition">
                    <div class="flex justify-between items-start mb-3">
                        <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2.5 py-1 rounded-md border border-qatar-maroon/20">وزارة الصحة العامة</span>
                        <span class="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded">مكافأة: 500 نقطة جدارة</span>
                    </div>
                    <h3 class="text-base font-black text-slate-800 mb-2">أتمتة تجربة المراجعين باستخدام الذكاء الاصطناعي في المراكز الصحية</h3>
                    <p class="text-xs text-slate-500 leading-relaxed mb-4">
                        المطلوب: تصميم نموذج أولي لتقليل مدة انتظار المراجعين بنسبة 35% بالاعتماد على خوارزميات التنبؤ المستفادة من مقررات Coursera.
                    </p>
                    <div class="flex items-center justify-between pt-3 border-t border-slate-100 text-xs">
                        <span class="text-slate-400"><i class="fa-regular fa-clock ml-1"></i> متبقي 12 يوماً للتقديم</span>
                        <button onclick="submitChallenge('أتمتة تجربة المراجعين')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white font-bold px-4 py-2 rounded-lg transition shadow-xs">
                            تقديم مقترح الحل +
                        </button>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs hover:border-qatar-maroon/50 transition">
                    <div class="flex justify-between items-start mb-3">
                        <span class="bg-qatar-maroonSoft text-qatar-maroon text-[10px] font-bold px-2.5 py-1 rounded-md border border-qatar-maroon/20">وزارة البلدية</span>
                        <span class="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded">مكافأة: 450 نقطة جدارة</span>
                    </div>
                    <h3 class="text-base font-black text-slate-800 mb-2">لوحة ذكية موحدة لرصد ومتابعة كفاءة استهلاك الطاقة بالمنشآت البلدية</h3>
                    <p class="text-xs text-slate-500 leading-relaxed mb-4">
                        المطلوب: توظيف مهارات ذكاء الأعمال (PowerBI / Tableau) لدمج قراءات العدادات الذكية وإصدار تنبيهات فورية للهدر.
                    </p>
                    <div class="flex items-center justify-between pt-3 border-t border-slate-100 text-xs">
                        <span class="text-slate-400"><i class="fa-regular fa-clock ml-1"></i> متبقي 19 يوماً للتقديم</span>
                        <button onclick="submitChallenge('لوحة ذكية لاستهلاك الطاقة')" class="bg-qatar-maroon hover:bg-qatar-maroonDark text-white font-bold px-4 py-2 rounded-lg transition shadow-xs">
                            تقديم مقترح الحل +
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- الشاشة 6: بوابة الجهة الحكومية B2B (مستوحاة من FutureX)    -->
        <!-- ========================================================= -->
        <section id="view-entity-view" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <div class="inline-flex items-center gap-1.5 bg-qatar-maroonSoft text-qatar-maroon text-xs font-bold px-3 py-1 rounded-full mb-2 border border-qatar-maroon/20">
                            <i class="fa-solid fa-building-columns"></i> بوابة الإدارة المؤسسية B2B
                        </div>
                        <h2 class="text-xl font-black text-slate-800">لوحة تحكم: وزارة الاتصالات وتكنولوجيا المعلومات</h2>
                        <p class="text-xs text-slate-500 mt-1">متابعة استهلاك رخص Coursera، نسب التزام الموظفين بالمسارات، وتصدير تقارير الإنجاز لديوان الخدمة المدنية</p>
                    </div>
                    <div class="flex gap-2">
                        <button onclick="showToast('جاري تصدير التقرير التنفيذي بصيغة Excel...')" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl transition flex items-center gap-2">
                            <i class="fa-solid fa-file-excel"></i> تصدير تقرير موارد
                        </button>
                    </div>
                </div>
            </div>

            <!-- إحصائيات الجهة الحكومية -->
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                    <span class="text-xs font-bold text-slate-500 block mb-1">إجمالي الموظفين المسجلين</span>
                    <span class="text-2xl font-black text-slate-800">1,240</span>
                    <span class="text-[10px] text-emerald-600 font-bold block mt-1">+85 انضموا هذا الشهر</span>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                    <span class="text-xs font-bold text-slate-500 block mb-1">نسبة استهلاك رخص Coursera</span>
                    <span class="text-2xl font-black text-qatar-maroon">92%</span>
                    <span class="text-[10px] text-slate-400 font-bold block mt-1">460 من أصل 500 رخصة</span>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                    <span class="text-xs font-bold text-slate-500 block mb-1">ساعات التدريب المنجزة</span>
                    <span class="text-2xl font-black text-slate-800">14,850</span>
                    <span class="text-[10px] text-emerald-600 font-bold block mt-1">متوسط 12 ساعة / موظف</span>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
                    <span class="text-xs font-bold text-slate-500 block mb-1">نسبة إتمام المسارات المرنة</span>
                    <span class="text-2xl font-black text-slate-800">68%</span>
                    <span class="text-[10px] text-qatar-maroon font-bold block mt-1">أعلى من المستهدف الوطني (+8%)</span>
                </div>
            </div>

            <!-- جدول تتبع الموظفين -->
            <div class="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
                <div class="p-5 border-b border-slate-100 flex justify-between items-center">
                    <h3 class="font-black text-sm text-slate-800">سجل نشاط الكفاءات بالوزارة (محدث لحظياً)</h3>
                    <span class="text-xs text-slate-500 font-semibold">عرض أحدث 4 موظفين</span>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-right text-xs">
                        <thead class="bg-slate-50 text-slate-600 font-bold border-b border-slate-100">
                            <tr>
                                <th class="p-4">اسم الموظف</th>
                                <th class="p-4">المسمى الوظيفي</th>
                                <th class="p-4">المسار التدريبي</th>
                                <th class="p-4">الساعات المنجزة</th>
                                <th class="p-4">نقاط الجدارة</th>
                                <th class="p-4">حالة المواءمة</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="p-4 font-bold text-slate-800">م. ناصر الكعبي</td>
                                <td class="p-4">مستشار رقمي</td>
                                <td class="p-4 text-qatar-maroon font-semibold">حوكمة الذكاء الاصطناعي</td>
                                <td class="p-4 font-bold">62.5 س</td>
                                <td class="p-4 font-black text-qatar-maroon">3,450</td>
                                <td class="p-4"><span class="bg-emerald-100 text-emerald-800 px-2.5 py-0.5 rounded-full text-[10px] font-bold">متطابق مع خطة موارد</span></td>
                            </tr>
                            <tr>
                                <td class="p-4 font-bold text-slate-800">د. مريم السادة</td>
                                <td class="p-4">مدير إدارة النظم</td>
                                <td class="p-4 text-qatar-maroon font-semibold">الأمن السيبراني المتقدم</td>
                                <td class="p-4 font-bold">48.0 س</td>
                                <td class="p-4 font-black text-qatar-maroon">2,910</td>
                                <td class="p-4"><span class="bg-emerald-100 text-emerald-800 px-2.5 py-0.5 rounded-full text-[10px] font-bold">متطابق مع خطة موارد</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- الشاشة 7: إدارة ملفات Excel الخمسة وفحص جودة ومواءمة البيانات -->
        <!-- ========================================================= -->
        <section id="view-admin-excel-view" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-800 text-xs font-bold px-3 py-1 rounded-full mb-2">
                            <i class="fa-solid fa-file-excel"></i> محرك استيراد وتدقيق البيانات المعتمدة
                        </div>
                        <h2 class="text-xl font-black text-slate-800">مركز مراجعة وجودة ملفات الإكسل (Excel 5 Hub)</h2>
                        <p class="text-xs text-slate-500 mt-1">
                            فحص ومطابقة ملفات البرامج، الكفاءات الثلاث (سلوكية، قيادية، فنية)، والمواءمة المنجزة دون تعديل البيانات الأصلية تلقائياً.
                        </p>
                    </div>
                    <div class="flex gap-2">
                        <button onclick="document.getElementById('excel-file-upload').click()" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl transition flex items-center gap-2">
                            <i class="fa-solid fa-cloud-arrow-up"></i> استيراد ملف إكسل جديد
                        </button>
                        <input type="file" id="excel-file-upload" class="hidden" accept=".xlsx, .xls, .csv" onchange="simulateExcelUpload(this)">
                    </div>
                </div>
            </div>

            <!-- بطاقات حالة الملفات الخمسة المرجعية -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
                    <div class="text-[10px] font-bold text-slate-400">الملف 1</div>
                    <div class="text-xs font-black text-slate-800 mt-0.5">جميع البرامج التدريبية</div>
                    <div class="text-emerald-600 text-[11px] font-bold mt-2"><i class="fa-solid fa-check"></i> 450 برنامجاً موثقاً</div>
                </div>
                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
                    <div class="text-[10px] font-bold text-slate-400">الملف 2</div>
                    <div class="text-xs font-black text-slate-800 mt-0.5">الكفاءات الوظيفية</div>
                    <div class="text-emerald-600 text-[11px] font-bold mt-2"><i class="fa-solid fa-check"></i> سلوكية، قيادية، فنية</div>
                </div>
                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
                    <div class="text-[10px] font-bold text-slate-400">الملف 3</div>
                    <div class="text-xs font-black text-slate-800 mt-0.5">مواءمة البرامج والكفاءات</div>
                    <div class="text-emerald-600 text-[11px] font-bold mt-2"><i class="fa-solid fa-check"></i> مطابقة بنسبة 100%</div>
                </div>
                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
                    <div class="text-[10px] font-bold text-slate-400">الملف 4</div>
                    <div class="text-xs font-black text-slate-800 mt-0.5">مستويات الكفاءة والبرامج</div>
                    <div class="text-emerald-600 text-[11px] font-bold mt-2"><i class="fa-solid fa-check"></i> 4 مستويات معتمدة</div>
                </div>
                <div class="bg-white p-4 rounded-xl border border-amber-200 bg-amber-50/50 shadow-xs">
                    <div class="text-[10px] font-bold text-amber-700">الملف 5</div>
                    <div class="text-xs font-black text-slate-800 mt-0.5">المجموعات والمسميات</div>
                    <div class="text-amber-700 text-[11px] font-bold mt-2"><i class="fa-solid fa-triangle-exclamation"></i> 3 مسميات بحاجة لمواءمة</div>
                </div>
            </div>

            <!-- جدول رصد جودة البيانات والتعارضات (دون مساس بالبيانات الأصلية) -->
            <div class="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
                <div class="p-5 border-b border-slate-100 flex justify-between items-center">
                    <h3 class="font-black text-sm text-slate-800">سجل تدقيق جودة البيانات (Data Integrity & Discrepancies)</h3>
                    <span class="text-xs text-slate-500 font-semibold">تنبيهات النظام الذكية دون تعديل تلقائي</span>
                </div>
                <div class="p-5 space-y-3">
                    <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 text-xs flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-triangle-exclamation text-amber-600 text-base"></i>
                            <div>
                                <strong class="text-slate-800">بيانات غير مكتملة في الملف 5:</strong> المسمى الوظيفي "محلل استدامة بيئية" غير مقترن بكفاءة فنية صريحة.
                            </div>
                        </div>
                        <span class="bg-white text-amber-800 font-bold px-2.5 py-1 rounded border border-amber-200">معلق للمراجعة اليدوية</span>
                    </div>

                    <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 text-xs flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-600 text-base"></i>
                            <div>
                                <strong class="text-slate-800">اكتمال الربط:</strong> تم التحقق من ربط 450 برنامج تدريبي بروابط Coursera ومصفوفة الجدارات الحكومية بنجاح.
                            </div>
                        </div>
                        <span class="bg-white text-emerald-800 font-bold px-2.5 py-1 rounded border border-emerald-200">سليم ومعتمد</span>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- ========================================================= -->
    <!-- نافذة منبثقة: خريطة الرحلة التعليمية للمسار (Learning Journey) -->
    <!-- ========================================================= -->
    <div id="journey-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-3xl w-full border-2 border-qatar-maroon shadow-2xl overflow-hidden animate-scale">
            <div class="maroon-gradient p-6 text-white relative">
                <button onclick="closeModal('journey-modal')" class="absolute left-5 top-5 w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 text-white flex items-center justify-center transition">
                    <i class="fa-solid fa-x
