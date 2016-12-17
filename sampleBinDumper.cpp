/*
 * Copyright (c) 2016 Hailin Su, ISU NBCEC
 *
 * This file is part of sampleBinDumper.
 *
 * sampleBinDumper is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * sampleBinDumper is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU General Lesser Public License
 * along with sampleBinDumper. If not, see <http://www.gnu.org/licenses/>.
 */

//
//  sampleBinDumper.cpp
//  libHailins
//
//  Created by Hailin Su on 12/17/15.
//

#include <iostream>
#include <cstdlib>  // for exit()
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main(int argc, char** argv)
{
    if(argc!=2)
    {
        cerr << "sampleBinDumper 20151217" << endl;
        cerr << "syntax:" << endl;
        cerr << "    sampleBinDumper fileName [ > redirectFile ]" << endl;
        cerr << "Prints out the content of a binary MCMC sample file." << endl;
        exit(0);
    }

    ifstream infs(argv[1], ofstream::binary);
    if(!infs)
    {
        cerr << " [X] FILE NOT FOUND: couldn't open file to read: " << argv[1] << endl;
        exit (-1);
    }

    char header[16];
    unsigned n1;    // number of samples
    unsigned n2;    // number of elements in each sample
    vector<float> vecSample;

    // read if the parameter is 'SAMP'
    infs.read(header, 4);
    header[4]=0;
    string h (header);
    if(h!="SAMP")
    {
        infs.close();
        cerr << " [X] HEADER MISMATCH: the given file " << argv[1] << " is not a valid binary sample file." << endl;
        exit (-1);
    }

    // read number of samples
    infs.read((char*)&n1, sizeof(n1));
    // read number of elements in each sample, twice
    infs.read((char*)&n2, 2*sizeof(n2));
    // resize work vector to store each sample
    vecSample.resize(n2);
    unsigned sampleSize (n2*sizeof(float)), i;

    while (infs.read((char*)vecSample.data(), sampleSize))
    {
        for(i=0; i<n2; ++i)
            cout << setfill(' ') << setw(8) << setprecision(4) << fixed << right << vecSample[i] << " ";
        cout << endl;
    }
    infs.close();
}
