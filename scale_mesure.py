import sys
from fractions import Fraction
from decimal import Decimal

scale = 2.0/5.0
result = float(sys.argv[1])*scale
#fraq = result.as_integer_ratio()
#result_fraq = str(int(result))+" "+str(fraq)
print( sys.argv[1] +" at scale "+ str(scale) +" is " )
print( str(result) +" inches or "+ str(result/12) +"feet.")