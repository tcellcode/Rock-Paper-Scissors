def main():
    eq = input('Type equation, format:\n2*x + 6*y = 8\n>> ')
    eq = eq.split('=')
    sym = input('Type all symbols, format:\nx y z\n>> ')
    all_sym = sym.split()


    exe_file = f'''
from sympy import symbols, Eq
from sympy.solvers import solve

{sym.replace(' ', ' , ')} = symbols('{sym}')

for item in {all_sym}:
    x = eval('{eq[0]}')
    y = eval('{eq[1]}') 
    print(item, ' = ', solve ( Eq(x,y) , symbols(item) , dict=True)  ) 
    '''

    exec(exe_file)

    ex = input('Enter something to exit, "again" to continue.\n>> ')
    if ex == 'again':
        main()
        
if __name__ == '__main__':
    main()
