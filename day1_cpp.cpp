#include <fstream>
#include <string>
#include <iostream>
int main()
{
    std::ifstream myfile;
    myfile.open("day1.txt");
    std::string nums = "123456789";
    int count = 0;
    while (myfile.good())
    {
        std::string str;
        myfile >> str;
        std::string digits = "";
        for (char c : str)
        {
            for (char n : nums)
            {
                if (c == n)
                    digits += c;
            }
        }
        if (digits != "")
        {
            std::cout << digits << std::endl;
            std::string f = "";
            f.push_back(digits[0]);
            f.push_back(digits[digits.length() - 1]);
            int new_digits = stoi(f);
            count += new_digits;
        }
    }
    std::cout << count << std::endl;
}