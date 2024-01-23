echo "Alexandria Skinner
User: $USER"

gunzip -c dictionary | grep -E "^[acmfuot]*a[acmfuot]*" | grep -E "...." | wc

gunzip -c dictionary | grep -E "^[tabilrn]*b[tabilrn]*" | grep -E "...." | wc

gunzip -c dictionary | grep -E "^[maocdin]*c[maocdin]*" | grep -E "...." | wc

gunzip -c dictionary | grep -E "^[anozigr]*z[anozigr]*" | grep -E "...." | wc
