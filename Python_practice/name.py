from hello_name import name
name("AJ")

total_seconds = 3685
hours = total_seconds // (60*60)
minutes = total_seconds % (60*60) // 60
seconds = total_seconds % (60*60) % 60
print(hours)
print(minutes)
print(seconds)