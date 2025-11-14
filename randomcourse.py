import random
import string

# برگرداندن یک مقدار رندوم بین صفر و یک
print(random.random()) 

# از محدوده داده شده یک مقدار رندوم را بر میگرداند
print(random.randint(10, 100)) # int
print(random.uniform(10, 100)) # float


# مثلا یک لیست داریم و یک ایتم رو به صورت رندوم برمیگرداند
print(random.choice([1, 2, 8, 9]))

# اگر بیشتر از یک مقدار رندوم خواستیم از این متد استفاده میکنیم
print(random.choices(("an;opwoew9igjo90[abbr"),k=10))

#برای تبدیل کردن لیست خروجی به استرینگ 
print("".join(random.choices(("an;opwoew9igjo90[abbr"),k=10)))

# اگر در بالا استرینگ خالی نمدادیم با استفاده از اون عناصر لیست ما رو به هم ملحق میکرد
print("_".join(random.choices(("an;opwoew9igjo90[abbr"),k=10)))


# ساخت یک پسوورد رندوم با استفاده از مازول استرینگ
print("".join(random.choices((string.ascii_letters + string.digits),k=10)))

# این متد لیست ما را بهم میریزد 
# این متد واقعا لیست را تغییر میدهد و دستکاری میکند به جای نتیجه برگرداندن
numbers  = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)

# بدون تکرار رندوم
print(random.sample(numbers, k=2))


# ثابت نگه داشتن خروجی ها برای تست
random.seed(500)