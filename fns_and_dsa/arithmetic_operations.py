#Arithmetic Operatoins functions
def perform_operation(num1, num2, operation):
	match operation:
        	case "add":
            		return num1+num2
	        case "subtract":
        		return num1-num2
	        case "multiply":
           		return num1*num2
	        case "divide":
	       		return num1/num2
