#!/bin/bash

count_amount_number(cases){
    count = 0
    while [cases != 0]
    do
        cases = $(($cases/10))
        ((count++))
    done

    return $count

}
check_number(cases){
    case count_amount_number($cases) in

    1)
        return "0000$cases"
        ;;
    2)
        return "000$cases"
        ;;
    3)
        return "00$cases"
        ;;
    4)  
        return "0$cases"
        ;;

    esac       
}

rename_dir(cases){
   path="BraTS2021_$cases" 
   

}