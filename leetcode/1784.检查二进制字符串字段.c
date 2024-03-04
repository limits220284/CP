bool checkOnesSegment(char * s){
    int l = 0, r = strlen(s)-1;

    while (s[l] == '1') l++;
    while (s[r] == '0') r--;

    return l-r == 1;
}