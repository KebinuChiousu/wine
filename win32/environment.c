/*
 * Win32 kernel functions
 *
 * Copyright 1995 Martin von Loewis and Cameron Heide
 */

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "windows.h"
#include "winerror.h"
#include "kernel32.h"
#include "module.h"
#include "task.h"
#include "stddebug.h"
#include "debug.h"


/***********************************************************************
 *           GetCommandLineA      (KERNEL32.161)
 */
LPSTR GetCommandLineA(void)
{
    static char buffer[256];
    char *cp;
    PDB *pdb = (PDB *)GlobalLock16( GetCurrentPDB() );

    lstrcpyn32A( buffer, MODULE_GetModuleName( GetExePtr(GetCurrentTask()) ),
                 sizeof(buffer) - 1 );
    cp = buffer + strlen(buffer);
    if (pdb->cmdLine[0])
    {
        *cp++ = ' ';
        memcpy( cp, &pdb->cmdLine[1], pdb->cmdLine[0] );
    }
    dprintf_win32(stddeb,"CommandLine = %s\n", buffer );
    return buffer;
}


/***********************************************************************
 *           GetSystemPowerStatus      (KERNEL32.621)
 */
BOOL GetSystemPowerStatus(LPSYSTEM_POWER_STATUS sps_ptr)
{
    return FALSE;   /* no power management support */
}


/***********************************************************************
 *           SetSystemPowerState      (KERNEL32.630)
 */
BOOL SetSystemPowerState(BOOL suspend_or_hibernate, BOOL force_flag)
{
    /* suspend_or_hibernate flag: w95 does not support
       this feature anyway */

    for ( ;0; )
    {
        if ( force_flag )
        {
        }
        else
        {
        }
    }
    return TRUE;
}

