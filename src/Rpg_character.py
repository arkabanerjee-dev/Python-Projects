full_dot = '●'
empty_dot = '○'

def create_character (character_name,strength,intelligence,charisma):
   
        if not isinstance(character_name,str) :
            return "The character name should be a string"

        if not character_name:
            # empty string check as "" is falsly value in python
            return "The character should have a name"

        if  len(character_name)>10 :
            return "The character name is too long"
            
        if " " in character_name :
            return"The character name should not contain spaces"
            

        # validating the stats 

        if not isinstance(strength,int) and not isinstance(intelligence,int) and not isinstance(charisma,int):
            return "All stats should be integers"
            
        if strength<1 or intelligence<1 or charisma<1 :
            return "All stats should be no less than 1"

        if strength>4 or intelligence>4 or charisma>4 :
            return "All stats should be no more than 4"

        if strength+intelligence+charisma != 7 :
            return "The character should start with 7 points"
        
        # if return statement not hit yet all verifications passed 

        # return f"{character_name}\nSTR {full_dot*strength}{empty_dot*(10-strength)}\nINT  {full_dot*intelligence}{empty_dot*(10-intelligence)}\nCHA {full_dot*charisma}{empty_dot*(10-charisma)}"
        answer = (character_name
                +'\nSTR ' +full_dot*(strength)+empty_dot*(10-strength)
                +'\nINT ' +full_dot*(intelligence)+empty_dot*(10-intelligence)
                +'\nCHA ' +full_dot*(charisma)+empty_dot*(10-charisma) )
        return answer

ans=create_character("sibasi",2 ,2,3) 
print(ans) 
