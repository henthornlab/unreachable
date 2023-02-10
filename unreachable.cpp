#ifdef DEATH
    #define DEATH 1
#else
    #define DEATH 0
#endif

#include <iostream>

int main() {
    if (!DEATH) {
        std::cout << "You chose to live! But alas, you didn't get the flag.\n";
        return 0;
    }
    // So you have chosen death
    while(1) ;
}

void the_unreachable_flag() {
    
    std::cout << "You've reached the unreachable code\n";
    std::cout << "The flag is " << "xxxxxx" << "\n";
}



