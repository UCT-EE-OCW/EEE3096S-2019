#include <stdio.h>
#include "Timer.h"
#include "globals.h"

extern __fp16 data [625];
extern __fp16 carrier[625];

__fp16 result [625];

int main(int argc, char**argv){
    //double half = 1.5f;
    //printf("Type double\n");
    //printf("precision %f\n", half);
    //printf("precision sizeof %d\n", sizeof(half));
    //printf("precision %f\n", half);
    //printf("precision 0x%04x\n", *(short*)(void*)&half);
    
   printf("__fp16, neonfp16\n");
   tic(); // start the timer
   for (int i = 0;i<625;i++ ){
       result[i] = data[i] * carrier[i];
   } 
    double t = toc();
   printf("Time %lf\n",t);
   
    return 0;
}
