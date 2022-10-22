from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

A, B = map(float, input().split())

val = float(B/A)
ans = Decimal(str(val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

print("{:.3f}".format(ans))