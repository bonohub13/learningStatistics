#include <iostream>
#include <vector>
#include <string>
#include <cmath>

double mean(std::vector<double> &datas)
{
    double output = 0;

    for (auto& data: datas)
    {
        output += data;
    }

    return output/datas.size();
}

double dist_unbiased(std::vector<double> &datas, double &mean)
{
    double output = 0;

    for (auto& data : datas)
    {
        output = std::pow(data - mean, 2);
    }

    return output/(datas.size() - 1);
}

int main(int argc, char** argv)
{
    int check = 0;
    char begin = '0', end = '9';
    std::vector<int> inputs;
    std::vector<double> datas;

    if (argc > 1)
    {
        for (uint i=1; i<argc; i++)
        {
            for (auto& chr : std::string(argv[i]))
            {
                if (chr < begin or chr > end)
                    check++;
            }
            if (check == 0)
                inputs.push_back(std::atoi(argv[i]));
            else
            {
                std::cout << "invalid argument" << std::endl;
                std::abort();
            }
        }
        if (inputs.size() != 2)
        {
            std::cout << "invalid number of arguments. Must be in this format. ([size of data], [maximum value of data])" << std::endl;
            std::abort();
        }

        while (datas.size() < inputs[0])
        {
            datas.push_back(std::rand()/inputs[1] / std::rand()/10);
        }

        auto datas_mean = mean(datas);
        std::cout << "mean: " << datas_mean << std::endl;

        auto datas_dist = dist_unbiased(datas, datas_mean);
        std::cout << "dist: " << datas_dist << std::endl;
    }
}
