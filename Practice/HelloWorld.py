import argparse

parser = argparse.ArgumentParser(
    prog = 'HelloWorld.py',
    description='Que quieres imprimir?',
)
# parser.add_argument("-n1", "--num1", default=0)
# parser.add_argument("-n2", "--num2", default=0)
# args = parser.parse_args()
# if (int(args.num1) < 0 or int(args.num2) < 0):
#     print("error")
# else:
#     sum = int(args.num1) + int(args.num2)
#     print(sum)

parser.add_argument("-c", "--country")
args = parser.parse_args()
Asia = {"Japan":"日本", "Korea":"韓国", "China":"中国", "Vietnam":"ベトナム", "India":"インド"}
i = False
for key, value in Asia.items():
    if key == args.country:
        i = True
        break
if i == True:
    print(value + "はアジアです")
else:
    print("アジアではありません")