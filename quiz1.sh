# Authors: Christina Chen, Alexandria Skinner
echo "Alexandria Skinner
User: $USER"

gunzip -c dictionary | grep -E "^[acmfuot]*a[acmfuot]*" | grep -E "...." | wc

gunzip -c dictionary | grep -E "^[tabilrn]*b[tabilrn]*" | grep -E "...." | wc

gunzip -c dictionary | grep -E "^[maocdin]*c[maocdin]*" | grep -E "...." | wc

gunzip -c dictionary | grep -E "^[anozigr]*z[anozigr]*" | grep -E "...." | wc

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep -E "tax_group"| sort -n | uniq -c
