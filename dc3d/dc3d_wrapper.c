#include <stdio.h>
void dc3d_(float *alpha, float *x, float *y, float *z, float *depth, float *dip, float *al1, float *al2, float *aw1, float *aw2, float *disl1, float *disl2, float *disl3,
float *ux, float *uy, float *uz, float *uxx, float *uyx, float *uzx, float *uxy, float *uyy, float *uzy, float *uxz, float *uyz, float *uzz, int *iret);
float ux(float alpha, float x, float y, float z, float depth, float dip, float al1, float al2, float aw1, float aw2, float disl1, float disl2, float disl3)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d_(&alpha, &x, &y, &z, &depth, &dip, &al1, &al2, &aw1, &aw2, &disl1, &disl2, &disl3,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return ux;
}
float uy(float alpha, float x, float y, float z, float depth, float dip, float al1, float al2, float aw1, float aw2, float disl1, float disl2, float disl3)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d_(&alpha, &x, &y, &z, &depth, &dip, &al1, &al2, &aw1, &aw2, &disl1, &disl2, &disl3,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return uy;
}
float uz(float alpha, float x, float y, float z, float depth, float dip, float al1, float al2, float aw1, float aw2, float disl1, float disl2, float disl3)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d_(&alpha, &x, &y, &z, &depth, &dip, &al1, &al2, &aw1, &aw2, &disl1, &disl2, &disl3,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return uz;
}

