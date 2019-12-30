plain,encrypted=input().split()
encrypted_info={}
can_encrypted=True

if len(plain)==len(encrypted):
    for i in range(len(plain)):
        plain_char=plain[i]
        encrypted_char=encrypted[i]

        if plain_char in encrypted_info:
            if not encrypted_char==encrypted_info[plain_char]:
                can_encrypted=False

        else:
            encrypted_info[plain_char]=encrypted_char

        if not can_encrypted:
            break

else:
    can_encrypted=False


if can_encrypted:
    print("True "+str(encrypted_info))

else:
    print("False")

            
