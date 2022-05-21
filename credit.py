import re


CREDIT_CARD_BANKS = {

    '37': 'AMEX',
    '34': 'AMEX',
    '51': 'MASTERCARD',
    '52': 'MASTERCARD',
    '53': 'MASTERCARD',
    '54': 'MASTERCARD',
    '55': 'MASTERCARD',
    '4': 'VISA'

}

BANKS_ACCOUNTS = ['34','37','51','52','53','54','55','4']


amex_valid_long = 15
visa_valid1_long = 13
visa_valid2_long = 16
mastercard_valid_log = 16
sum = 0


#Usamos una expresio regular para validr que la cadena solo contenga valores numericos
#We use a regular expression to validate if the String is all numbers
def isANumber(str):
    return re.search(r'^[-+]?[0-9]+$', str)


def get_credit_card_addition(credit_number):
    

    #Se revirtio la tajeta de credito ya que el algotimo de Luhn empieza desde la derecha y se genera dos listas una the pares y de impares 
    #The credit number was revert because the Luhn Algorithm starts from mostright and generate two lists one is odd and the other is even
    odd_creadit_numbers = str(credit_number)[-1::-2]
    even_creadit_numbers = str(credit_number)[-2::-2]
    sum_even_values = 0
    sum_odd_values = 0 

    
    #Iteramos y multiplicamos los valores pares, si el número es mayar a 10 se suman los dos números
    #We iterate and multiply the even values, if the result is greater than 10 we add the two numbers
    for even_cred_card_num in even_creadit_numbers:
        
        credit_card_num = int(even_cred_card_num) * 2 
        
        if credit_card_num >= 10:
            
            c_nn = str(credit_card_num)
            credit_card_num = int(c_nn[0]) + int(c_nn[1])
            
        #We get the sum of all values
        #Se suman todos los valores
        sum_even_values += credit_card_num
 
    #Iteramos y sumamos los valores impares
    #We iterate and sum of even values
    for num in odd_creadit_numbers:
        sum_odd_values += int(num)


    return sum_odd_values + sum_even_values



def validate_credit_number(sum, credit_number):

    #Validamos que la suma de pares e impares sea multiplo de 10
    #Validate if the sum of even and odd values are 10 base
    if sum % 10 == 0:

        #Iteramos las cuentas de banco en un diccionario y validamos si la se encuentran dentro de los valores
        #Iterate the banks accout from a diccionary and validate if it exists
        for accounts in BANKS_ACCOUNTS:
            if str(credit_number).startswith(str(accounts)):
                if CREDIT_CARD_BANKS[str(accounts)] == "AMEX" and  len(str(credit_number)) == amex_valid_long:
                    print(CREDIT_CARD_BANKS[str(accounts)])
                elif CREDIT_CARD_BANKS[str(accounts)] == "VISA" and  (len(str(credit_number)) == visa_valid1_long or len(str(credit_number)) == visa_valid2_long):
                    print(CREDIT_CARD_BANKS[str(accounts)])
                elif CREDIT_CARD_BANKS[str(accounts)] == "MASTERCARD" and  len(str(credit_number)) == mastercard_valid_log:
                    print(CREDIT_CARD_BANKS[str(accounts)])
    else:
        print('INVALID')




#Intentamos validar la tarjeta de credito si contiene algun caracter diferente a número que no haga nada
#Try to validate the credit number, if contains a non number character, does nothing
try:
    credit_number = input('Inser your credit number: ')
    if isANumber:
        sum = get_credit_card_addition(credit_number)
        validate_credit_number(sum,credit_number)

except:
    pass


