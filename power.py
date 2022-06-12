class power:

    def expo(self,num, pow):
        
        if pow == 1 or pow == 0 or num == 1:
            return num
        elif pow == 0:
            return 1
        else:
            return (num**pow)

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    pow = int(input("Enter the power : "))
    power_obj = power()
    print(f"Output is : {power_obj.expo(num, pow)}")

