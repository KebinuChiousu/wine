/*
 * File handling declarations
 *
 * Copyright 1996 Alexandre Julliard
 */

#ifndef __WINE_FILE_H
#define __WINE_FILE_H

#include "windows.h"

extern void FILE_SetDosError(void);
extern void FILE_CloseAllFiles( HANDLE hPDB );
extern int FILE_Stat( LPCSTR unixName, BYTE *pattr, DWORD *psize,
                      WORD *pdate, WORD *ptime );
extern int FILE_GetDateTime( HFILE hFile, WORD *pdate, WORD *ptime,
                             BOOL refresh );
extern int FILE_SetDateTime( HFILE hFile, WORD date, WORD time );
extern int FILE_Fstat( HFILE hFile, BYTE *pattr, DWORD *psize,
                       WORD *pdate, WORD *ptime );
extern HFILE FILE_Dup( HFILE hFile );
extern HFILE FILE_Dup2( HFILE hFile1, HFILE hFile2 );
extern INT32 FILE_Read( HFILE hFile, LPVOID buffer, UINT32 count );
extern HFILE _lcreat_uniq( LPCSTR path, INT32 attr );

#endif  /* __WINE_FILE_H */
