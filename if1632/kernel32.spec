name	kernel32
type	win32
base	1

0000 stub AddAtomA
0001 stub AddAtomW
0002 stub AddConsoleAliasA
0003 stub AddConsoleAliasW
0004 stub AllocConsole
0005 stub AreFileApisANSI
0006 stub BackupRead
0007 stub BackupSeek
0008 stub BackupWrite
0009 stub BaseAttachCompleteThunk
0010 stub BasepDebugDump
0011 stdcall Beep(long long) Beep
0012 stub BeginUpdateResourceA
0013 stub BeginUpdateResourceW
0014 stub BuildCommDCBA
0015 stub BuildCommDCBAndTimeoutsA
0016 stub BuildCommDCBAndTimeoutsW
0017 stub BuildCommDCBW
0018 stub CallNamedPipeA
0019 stub CallNamedPipeW
0020 stub ClearCommBreak
0021 stub ClearCommError
0022 stub CloseConsoleHandle
0023    stdcall CloseHandle(long) CloseHandle
0024 stub CloseProfileUserMapping
0025 stub CmdBatNotification
0026 stub CommConfigDialogA
0027 stub CommConfigDialogW
0028 stub CompareFileTime
0029 stdcall CompareStringA(long long ptr long ptr long) CompareString32A
0030 stdcall CompareStringW(long long ptr long ptr long) CompareString32W
0031 stub ConnectNamedPipe
0032 stub ConsoleMenuControl
0033 stub ConsoleSubst
0034 stub ContinueDebugEvent
0035 stub ConvertDefaultLocale
0036 stub CopyFileA
0037 stub CopyFileW
0038 stub CreateConsoleScreenBuffer
0039 stdcall CreateDirectoryA(ptr ptr) CreateDirectory32A
0040 stub CreateDirectoryExA
0041 stub CreateDirectoryExW
0042 stdcall CreateDirectoryW(ptr ptr) CreateDirectory32W
0043 	stdcall CreateEventA(ptr long long ptr) CreateEventA
0044 stub CreateEventW
0045   stdcall CreateFileA(ptr long long ptr long long long) CreateFileA
0046 	stdcall CreateFileMappingA(long ptr long long long ptr) CreateFileMapping
0047 stub CreateFileMappingW
0048 stub CreateFileW
0049 stub CreateIoCompletionPort
0050 stub CreateMailslotA
0051 stub CreateMailslotW
0052 	stdcall CreateMutexA(ptr long ptr) CreateMutexA
0053 stub CreateMutexW
0054 stub CreateNamedPipeA
0055 stub CreateNamedPipeW
0056 stub CreatePipe
0057 stub CreateProcessA
0058 stub CreateProcessW
0059 stub CreateRemoteThread
0060 stub CreateSemaphoreA
0061 stub CreateSemaphoreW
0062 stub CreateTapePartition
0063 stub CreateThread
0064 stub CreateVirtualBuffer
0065 stub DebugActiveProcess
0066 stub DebugBreak
0067 stub DefineDosDeviceA
0068 stub DefineDosDeviceW
0069 stub DeleteAtom
0070 stdcall DeleteCriticalSection(ptr)	DeleteCriticalSection
0071 stdcall DeleteFileA(ptr) DeleteFile32A
0072 stdcall DeleteFileW(ptr) DeleteFile32W
0073 stub DeviceIoControl
0074 stub DisableThreadLibraryCalls
0075 stub DisconnectNamedPipe
0076 stub DosDateTimeToFileTime
0077 stub DuplicateConsoleHandle
0078 	stdcall DuplicateHandle(long long long ptr long long long) DuplicateHandle
0079 stub EndUpdateResourceA
0080 stub EndUpdateResourceW
0081 stdcall EnterCriticalSection(ptr)	EnterCriticalSection
0082 stub EnumCalendarInfoA
0083 stub EnumCalendarInfoW
0084 stub EnumDateFormatsA
0085 stub EnumDateFormatsW
0086 stub EnumResourceLanguagesA
0087 stub EnumResourceLanguagesW
0088 stub EnumResourceNamesA
0089 stub EnumResourceNamesW
0090 stub EnumResourceTypesA
0091 stub EnumResourceTypesW
0092 stub EnumSystemCodePagesA
0093 stub EnumSystemCodePagesW
0094 stub EnumSystemLocalesA
0095 stub EnumSystemLocalesW
0096 stub EnumTimeFormatsA
0097 stub EnumTimeFormatsW
0098 stub EraseTape
0099 stub EscapeCommFunction
0100   stdcall ExitProcess(long) ExitProcess
0101 stub ExitThread
0102 stub ExitVDM
0103 stub ExpandEnvironmentStringsA
0104 stub ExpandEnvironmentStringsW
0105 stub ExpungeConsoleCommandHistoryA
0106 stub ExpungeConsoleCommandHistoryW
0107 stub ExtendVirtualBuffer
0108 stub FatalAppExitA
0109 stub FatalAppExitW
0110 stub FatalExit
0111 stub FileTimeToDosDateTime
0112 stub FileTimeToLocalFileTime
0113 stub FileTimeToSystemTime
0114 stub FillConsoleOutputAttribute
0115 stub FillConsoleOutputCharacterA
0116 stub FillConsoleOutputCharacterW
0117 stub FindAtomA
0118 stub FindAtomW
0119 stub FindClose
0120 stub FindCloseChangeNotification
0121 stub FindFirstChangeNotificationA
0122 stub FindFirstChangeNotificationW
0123 stub FindFirstFileA
0124 stub FindFirstFileW
0125 stub FindNextChangeNotification
0126 stub FindNextFileA
0127 stub FindNextFileW
0128 stdcall FindResourceA(long ptr ptr) FindResource32A
0129 stub FindResourceExA
0130 stub FindResourceExW
0131 stdcall FindResourceW(long ptr ptr) FindResource32W
0132 stub FlushConsoleInputBuffer
0133 stdcall FlushFileBuffers(long) FlushFileBuffers
0134 stub FlushInstructionCache
0135 stub FlushViewOfFile
0136 stub FoldStringA
0137 stub FoldStringW
0138 stub FormatMessageA
0139 stub FormatMessageW
0140 stub FreeConsole
0141 stdcall FreeEnvironmentStringsA(ptr)	FreeEnvironmentStringsA
0142 stdcall FreeEnvironmentStringsW(ptr)	FreeEnvironmentStringsW
0143 stdcall FreeLibrary(long) FreeLibrary32
0144 stub FreeLibraryAndExitThread
0145 stdcall FreeResource(long) FreeResource32
0146 stub FreeVirtualBuffer
0147 stub GenerateConsoleCtrlEvent
0148    stdcall GetACP() GetACP
0149 stub GetAtomNameA
0150 stub GetAtomNameW
0151 stub GetBinaryType
0152 stub GetBinaryTypeA
0153 stub GetBinaryTypeW
0154    stdcall GetCPInfo(long ptr) GetCPInfo
0155 stub GetCommConfig
0156 stub GetCommMask
0157 stub GetCommModemStatus
0158 stub GetCommProperties
0159 stub GetCommState
0160 stub GetCommTimeouts
0161	stdcall GetCommandLineA()	GetCommandLineA
0162 stub GetCommandLineW
0163 stub GetCompressedFileSizeA
0164 stub GetCompressedFileSizeW
0165 stub GetComputerNameA
0166 stub GetComputerNameW
0167 stub GetConsoleAliasA
0168 stub GetConsoleAliasExesA
0169 stub GetConsoleAliasExesLengthA
0170 stub GetConsoleAliasExesLengthW
0171 stub GetConsoleAliasExesW
0172 stub GetConsoleAliasW
0173 stub GetConsoleAliasesA
0174 stub GetConsoleAliasesLengthA
0175 stub GetConsoleAliasesLengthW
0176 stub GetConsoleAliasesW
0177 stub GetConsoleCP
0178 stub GetConsoleCommandHistoryA
0179 stub GetConsoleCommandHistoryLengthA
0180 stub GetConsoleCommandHistoryLengthW
0181 stub GetConsoleCommandHistoryW
0182 stub GetConsoleCursorInfo
0183 stub GetConsoleDisplayMode
0184 stub GetConsoleFontInfo
0185 stub GetConsoleFontSize
0186 stub GetConsoleHardwareState
0187 stub GetConsoleInputWaitHandle
0188 stub GetConsoleMode
0189 stub GetConsoleOutputCP
0190 stub GetConsoleScreenBufferInfo
0191 stub GetConsoleTitleA
0192 stub GetConsoleTitleW
0193 stub GetCurrencyFormatA
0194 stub GetCurrencyFormatW
0195 stub GetCurrentConsoleFont
0196 stdcall GetCurrentDirectoryA(long ptr) GetCurrentDirectory32A
0197 stdcall GetCurrentDirectoryW(long ptr) GetCurrentDirectory32W
0198 stdcall GetCurrentProcess() GetCurrentProcess
0199 stdcall GetCurrentProcessId() GetCurrentThreadId
0200 	stdcall GetCurrentThread() GetCurrentThread
0201	stdcall GetCurrentThreadId()	GetCurrentThreadId
0202 stub GetDateFormatA
0203 stub GetDateFormatW
0204 stub GetDefaultCommConfigA
0205 stub GetDefaultCommConfigW
0206 	stdcall GetDiskFreeSpaceA(ptr ptr ptr ptr ptr) GetDiskFreeSpace32A
0207 	stdcall GetDiskFreeSpaceW(ptr ptr ptr ptr ptr) GetDiskFreeSpace32W
0208 stdcall GetDriveTypeA(ptr) GetDriveType32A
0209 stdcall GetDriveTypeW(ptr) GetDriveType32W
0210	stdcall GetEnvironmentStrings()	GetEnvironmentStrings
0211 stub GetEnvironmentStringsA
0212 	stdcall GetEnvironmentStringsW()		GetEnvironmentStringsW
0213    stdcall GetEnvironmentVariableA(ptr ptr long) GetEnvironmentVariableA
0214 stub GetEnvironmentVariableW
0215 stub GetExitCodeProcess
0216 stub GetExitCodeThread
0217 stdcall GetFileAttributesA(ptr)		GetFileAttributesA
0218 stub GetFileAttributesW
0219   stdcall GetFileInformationByHandle(long ptr) GetFileInformationByHandle
0220 stub GetFileSize
0221 stub GetFileTime
0222    stdcall GetFileType(long) GetFileType
0223 stub GetFullPathNameA
0224 stub GetFullPathNameW
0225 stub GetHandleInformation
0226 stub GetLargestConsoleWindowSize
0227    stdcall GetLastError() GetLastError
0228    stdcall GetLocalTime(ptr) GetLocalTime
0229 stdcall GetLocaleInfoA(long long ptr long) GetLocaleInfoA
0230 stub GetLocaleInfoW
0231 stdcall GetLogicalDriveStringsA(long ptr) GetLogicalDriveStrings32A
0232 stdcall GetLogicalDriveStringsW(long ptr) GetLogicalDriveStrings32W
0233 stdcall GetLogicalDrives() GetLogicalDrives
0234 stub GetMailslotInfo
0235	stdcall GetModuleFileNameA(long ptr long) GetModuleFileNameA
0236 stub GetModuleFileNameW
0237	stdcall GetModuleHandleA(ptr)	WIN32_GetModuleHandle
0238 stub GetModuleHandleW
0239 stub GetNamedPipeHandleStateA
0240 stub GetNamedPipeHandleStateW
0241 stub GetNamedPipeInfo
0242 stub GetNextVDMCommand
0243 stub GetNumberFormatA
0244 stub GetNumberFormatW
0245 stub GetNumberOfConsoleFonts
0246 stub GetNumberOfConsoleInputEvents
0247 stub GetNumberOfConsoleMouseButtons
0248    stdcall GetOEMCP() GetOEMCP
0249 stub GetOverlappedResult
0250 stub GetPriorityClass
0251 stdcall GetPrivateProfileIntA(ptr ptr long ptr) GetPrivateProfileInt
0252 stub GetPrivateProfileIntW
0253 stub GetPrivateProfileSectionA
0254 stub GetPrivateProfileSectionW
0255 stdcall GetPrivateProfileStringA(ptr ptr ptr ptr long ptr) GetPrivateProfileString
0256 stub GetPrivateProfileStringW
0257 stdcall GetProcAddress(long ptr) GetProcAddress32
0258 stdcall GetProcessAffinityMask(long ptr ptr)	GetProcessAffinityMask
0259 stdcall GetProcessHeap() GetProcessHeap
0260 stub GetProcessHeaps
0261 stub GetProcessShutdownParameters
0262 stub GetProcessTimes
0263 stub GetProcessWorkingSetSize
0264 	stdcall GetProfileIntA(ptr ptr long) GetProfileInt
0265 stub GetProfileIntW
0266 stub GetProfileSectionA
0267 stub GetProfileSectionW
0268 stdcall GetProfileStringA(ptr ptr ptr ptr long) GetProfileString
0269 stub GetProfileStringW
0270 stub GetQueuedCompletionStatus
0271 stdcall GetShortPathNameA(ptr ptr long) GetShortPathName32A
0272 stdcall GetShortPathNameW(ptr ptr long) GetShortPathName32W
0273 stdcall GetStartupInfoA(ptr) GetStartupInfoA
0274 stub GetStartupInfoW
0275	stdcall GetStdHandle(long)	GetStdHandle
0276 stub GetStringTypeA
0277 stub GetStringTypeExA
0278 stub GetStringTypeExW
0279 stub GetStringTypeW
0280 stdcall GetSystemDefaultLCID() GetSystemDefaultLCID
0281 stub GetSystemDefaultLangID
0282 stdcall GetSystemDirectoryA(ptr long) GetSystemDirectory32A
0283 stdcall GetSystemDirectoryW(ptr long) GetSystemDirectory32W
0284 stub GetSystemInfo
0285 	stdcall GetSystemTime(ptr) GetSystemTime
0286 stub GetSystemTimeAdjustment
0287 stub GetTapeParameters
0288 stub GetTapePosition
0289 stub GetTapeStatus
0290 stdcall GetTempFileNameA(ptr ptr long ptr) GetTempFileName32A
0291 stdcall GetTempFileNameW(ptr ptr long ptr) GetTempFileName32W
0292 stdcall GetTempPathA(long ptr) GetTempPath32A
0293 stdcall GetTempPathW(long ptr) GetTempPath32W
0294	stdcall GetThreadContext(long ptr)	GetThreadContext
0295 stub GetThreadLocale
0296 stub GetThreadPriority
0297 stub GetThreadSelectorEntry
0298 stub GetThreadTimes
0299 stdcall GetTickCount() GetTickCount
0300 stub GetTimeFormatA
0301 stub GetTimeFormatW
0302    stdcall GetTimeZoneInformation(ptr) GetTimeZoneInformation
0303 stdcall GetUserDefaultLCID() GetUserDefaultLCID
0304 stub GetUserDefaultLangID
0305 stub GetVDMCurrentDirectories
0306 stdcall GetVersion() GetVersion32
0307 stdcall GetVersionExA(ptr) GetVersionEx32A
0308 stdcall GetVersionExW(ptr) GetVersionEx32W
0309 stdcall GetVolumeInformationA(ptr ptr long ptr ptr ptr ptr long) GetVolumeInformation32A
0310 stdcall GetVolumeInformationW(ptr ptr long ptr ptr ptr ptr long) GetVolumeInformation32W
0311 stdcall GetWindowsDirectoryA(ptr long) GetWindowsDirectory
0312 stub GetWindowsDirectoryW
0313 stdcall GlobalAddAtomA(ptr) GlobalAddAtom32A
0314 stdcall GlobalAddAtomW(ptr) GlobalAddAtom32W
0315 stdcall GlobalAlloc(long long) GlobalAlloc32
0316 stdcall GlobalCompact(long) GlobalCompact32
0317 stdcall GlobalDeleteAtom(long) GlobalDeleteAtom
0318 stdcall GlobalFindAtomA(ptr) GlobalFindAtom32A
0319 stdcall GlobalFindAtomW(ptr) GlobalFindAtom32W
0320 stub GlobalFix
0321 stdcall GlobalFlags(long) GlobalFlags32
0322 stdcall GlobalFree(long) GlobalFree32
0323 stdcall GlobalGetAtomNameA(long ptr long) GlobalGetAtomName32A
0324 stdcall GlobalGetAtomNameW(long ptr long) GlobalGetAtomName32W
0325 stdcall GlobalHandle(ptr) GlobalHandle32
0326 stdcall GlobalLock(long) GlobalLock32
0327 stub GlobalMemoryStatus
0328 stdcall GlobalReAlloc(long long long) GlobalReAlloc32
0329 stdcall GlobalSize(long) GlobalSize32
0330 stub GlobalUnWire
0331 stub GlobalUnfix
0332 stdcall GlobalUnlock(long) GlobalUnlock32
0333 stub GlobalWire
0334 stdcall HeapAlloc(long long long) HeapAlloc
0335 stdcall HeapCompact(long long) HeapCompact
0336 stdcall HeapCreate(long long long)	HeapCreate
0337 stdcall HeapDestroy(long) HeapDestroy
0338 stdcall HeapFree(long long ptr) HeapFree
0339 stdcall HeapLock(long) HeapLock
0340 stdcall HeapReAlloc(long long ptr long) HeapReAlloc
0341 stdcall HeapSize(long long ptr) HeapSize
0342 stdcall HeapUnlock(long) HeapUnlock
0343 stdcall HeapValidate(long long ptr) HeapValidate
0344 stdcall HeapWalk(long ptr) HeapWalk
0345 stub InitAtomTable
0346 stdcall InitializeCriticalSection(ptr) InitializeCriticalSection
0347 stdcall InterlockedDecrement(ptr) InterlockedDecrement
0348 stdcall InterlockedExchange(ptr) InterlockedExchange
0349 stdcall InterlockedIncrement(ptr) InterlockedIncrement
0350 stub InvalidateConsoleDIBits
0351 stdcall IsBadCodePtr(ptr long)	WIN32_IsBadCodePtr
0352 stub IsBadHugeReadPtr
0353 stub IsBadHugeWritePtr
0354 stdcall IsBadReadPtr(ptr long)	WIN32_IsBadReadPtr
0355 stub IsBadStringPtrA
0356 stub IsBadStringPtrW
0357 stdcall IsBadWritePtr(ptr long)	WIN32_IsBadWritePtr
0358 return IsDBCSLeadByte 4 0
0359 stub IsDBCSLeadByteEx
0360 stub IsValidCodePage
0361 stub IsValidLocale
0362 stub LCMapStringA
0363 stub LCMapStringW
0364 stdcall LeaveCriticalSection(ptr)	LeaveCriticalSection
0365	stdcall LoadLibraryA(long)		LoadLibraryA
0366 stub LoadLibraryExA
0367 stub LoadLibraryExW
0368 stub LoadLibraryW
0369 stub LoadModule
0370 stdcall LoadResource(long long) LoadResource32
0371 stdcall LocalAlloc(long long) LocalAlloc32
0372 stdcall LocalCompact(long) LocalCompact32
0373 stub LocalFileTimeToFileTime
0374 stdcall LocalFlags(long) LocalFlags32
0375 stdcall LocalFree(long) LocalFree32
0376 stdcall LocalHandle(ptr) LocalHandle32
0377 stdcall LocalLock(long) LocalLock32
0378 stdcall LocalReAlloc(long long long) LocalReAlloc32
0379 stdcall LocalShrink(long long) LocalShrink32
0380 stdcall LocalSize(long) LocalSize32
0381 stdcall LocalUnlock(long) LocalUnlock32
0382 stub LockFile
0383 stub LockFileEx
0384 stdcall LockResource(long) LockResource32
0385 stub MapViewOfFile
0386 	stdcall MapViewOfFileEx(long long long long long long) MapViewOfFileEx
0387 stub MoveFileA
0388 stub MoveFileExA
0389 stub MoveFileExW
0390 stub MoveFileW
0391 stdcall MulDiv(long long long) MulDiv32
0392 stdcall MultiByteToWideChar(long long ptr long ptr long) MultiByteToWideChar
0393 stub OpenConsoleW
0394 stub OpenEventA
0395 stub OpenEventW
0396 stdcall OpenFile(ptr ptr long) OpenFile
0397 stdcall OpenFileMappingA(long long ptr) OpenFileMapping
0398 stub OpenFileMappingW
0399 stub OpenMutexA
0400 stub OpenMutexW
0401 stub OpenProcess
0402 stub OpenProfileUserMapping
0403 stub OpenSemaphoreA
0404 stub OpenSemaphoreW
0405 stub OutputDebugStringA
0406 stub OutputDebugStringW
0407 stub PeekConsoleInputA
0408 stub PeekConsoleInputW
0409 stub PeekNamedPipe
0410 stub PrepareTape
0411 stub PulseEvent
0412 stub PurgeComm
0413 stub QueryDosDeviceA
0414 stub QueryDosDeviceW
0415 stub QueryPerformanceCounter
0416 stub QueryPerformanceFrequency
0417 stub QueryWin31IniFilesMappedToRegistry
0418 stdcall RaiseException(long long long ptr) RaiseException
0419 stub ReadConsoleA
0420 stub ReadConsoleInputA
0421 stub ReadConsoleInputW
0422 stub ReadConsoleOutputA
0423 stub ReadConsoleOutputAttribute
0424 stub ReadConsoleOutputCharacterA
0425 stub ReadConsoleOutputCharacterW
0426 stub ReadConsoleOutputW
0427 stub ReadConsoleW
0428 stdcall ReadFile(long ptr long ptr ptr) ReadFile
0429 stub ReadFileEx
0430 stub ReadProcessMemory
0431 stub RegisterConsoleVDM
0432 stub RegisterWaitForInputIdle
0433 stub RegisterWowBaseHandlers
0434 stub RegisterWowExec
0435 	stdcall ReleaseMutex(long) ReleaseMutex
0436 stub ReleaseSemaphore
0437 stdcall RemoveDirectoryA(ptr) RemoveDirectory32A
0438 stdcall RemoveDirectoryW(ptr) RemoveDirectory32W
0439 	stdcall ResetEvent(long) ResetEvent
0440 stub ResumeThread
0441 stdcall RtlFillMemory(ptr long long) RtlFillMemory
0442 stdcall RtlMoveMemory(ptr ptr long) RtlMoveMemory
0443 stdcall RtlUnwind(ptr long ptr long) RtlUnwind
0444 stdcall RtlZeroMemory(ptr long) RtlZeroMemory
0445 stub ScrollConsoleScreenBufferA
0446 stub ScrollConsoleScreenBufferW
0447 stub SearchPathA
0448 stub SearchPathW
0449 stub SetCommBreak
0450 stub SetCommConfig
0451 stub SetCommMask
0452 stub SetCommState
0453 stub SetCommTimeouts
0454 stub SetComputerNameA
0455 stub SetComputerNameW
0456 stub SetConsoleActiveScreenBuffer
0457 stub SetConsoleCP
0458 stub SetConsoleCommandHistoryMode
0459 stdcall SetConsoleCtrlHandler(ptr long) SetConsoleCtrlHandler
0460 stub SetConsoleCursor
0461 stub SetConsoleCursorInfo
0462 stub SetConsoleCursorPosition
0463 stub SetConsoleDisplayMode
0464 stub SetConsoleFont
0465 stub SetConsoleHardwareState
0466 stub SetConsoleKeyShortcuts
0467 stub SetConsoleMaximumWindowSize
0468 stub SetConsoleMenuClose
0469 stub SetConsoleMode
0470 stub SetConsoleNumberOfCommandsA
0471 stub SetConsoleNumberOfCommandsW
0472 stub SetConsoleOutputCP
0473 stub SetConsolePalette
0474 stub SetConsoleScreenBufferSize
0475 stub SetConsoleTextAttribute
0476 stub SetConsoleTitleA
0477 stub SetConsoleTitleW
0478 stub SetConsoleWindowInfo
0479 stdcall SetCurrentDirectoryA(ptr) SetCurrentDirectory
0480 stub SetCurrentDirectoryW
0481 stub SetDefaultCommConfigA
0482 stub SetDefaultCommConfigW
0483 stub SetEndOfFile
0484 stdcall SetEnvironmentVariableA(ptr ptr) SetEnvironmentVariable32A
0485 stdcall SetEnvironmentVariableW(ptr ptr) SetEnvironmentVariable32W
0486 stdcall SetErrorMode(long) SetErrorMode
0487 	stdcall	SetEvent(long) SetEvent
0488 stub SetFileApisToANSI
0489 stub SetFileApisToOEM
0490 stub SetFileAttributesA
0491 stub SetFileAttributesW
0492    stdcall SetFilePointer(long long ptr long) SetFilePointer
0493 stub SetFileTime
0494    stdcall SetHandleCount(long) W32_SetHandleCount
0495 stub SetHandleInformation
0496 stub SetLastConsoleEventActive
0497    stdcall SetLastError(long) SetLastError
0498 stub SetLocalTime
0499 stdcall SetLocaleInfoA(long long ptr) SetLocaleInfoA
0500 stub SetLocaleInfoW
0501 stub SetMailslotInfo
0502 stub SetNamedPipeHandleState
0503 stub SetPriorityClass
0504 stub SetProcessShutdownParameters
0505 stub SetProcessWorkingSetSize
0506 stub SetStdHandle
0507    stdcall SetSystemTime(ptr) SetSystemTime
0508 stub SetSystemTimeAdjustment
0509 stub SetTapeParameters
0510 stub SetTapePosition
0511 stdcall SetThreadAffinityMask(long long)	SetThreadAffinityMask
0512 stub SetThreadContext
0513 stub SetThreadLocale
0514 stub SetThreadPriority
0515    stdcall SetTimeZoneInformation(ptr) SetTimeZoneInformation
0516    stdcall SetUnhandledExceptionFilter(ptr) SetUnhandledExceptionFilter
0517 stub SetVDMCurrentDirectories
0518 stub SetVolumeLabelA
0519 stub SetVolumeLabelW
0520 stub SetupComm
0521 stub ShowConsoleCursor
0522 stdcall SizeofResource(long long) SizeofResource32
0523 	stdcall Sleep(long) Sleep
0524 stub SleepEx
0525 stub SuspendThread
0526 stub SystemTimeToFileTime
0527 stub SystemTimeToTzSpecificLocalTime
0528 stub TerminateProcess
0529 stub TerminateThread
0530 stdcall TlsAlloc()	TlsAlloc
0531 stdcall TlsFree(long)	TlsFree
0532 stdcall TlsGetValue(long)	TlsGetValue
0533 stdcall TlsSetValue(long ptr)	TlsSetValue
0534 stub TransactNamedPipe
0535 stub TransmitCommChar
0536 stub TrimVirtualBuffer
0537    stdcall UnhandledExceptionFilter(ptr) UnhandledExceptionFilter
0538 stub UnlockFile
0539 stub UnlockFileEx
0540 stub UnmapViewOfFile
0541 stub UpdateResourceA
0542 stub UpdateResourceW
0543 stub VDMConsoleOperation
0544 stub VDMOperationStarted
0545 stub VerLanguageNameA
0546 stub VerLanguageNameW
0547 stub VerifyConsoleIoHandle
0548    stdcall VirtualAlloc(ptr long long long) VirtualAlloc
0549 stub VirtualBufferExceptionHandler
0550    stdcall VirtualFree(ptr long long) VirtualFree
0551 stub VirtualLock
0552 stub VirtualProtect
0553 stub VirtualProtectEx
0554 stub VirtualQuery
0555 stub VirtualQueryEx
0556 stub VirtualUnlock
0557 stub WaitCommEvent
0558 stub WaitForDebugEvent
0559 stub WaitForMultipleObjects
0560 stub WaitForMultipleObjectsEx
0561 	stdcall WaitForSingleObject(long long) WaitForSingleObject
0562 stub WaitForSingleObjectEx
0563 stub WaitNamedPipeA
0564 stub WaitNamedPipeW
0565 stdcall WideCharToMultiByte(long long ptr long ptr long ptr ptr)	WideCharToMultiByte
0566 stub WinExec
0567 stub WriteConsoleA
0568 stub WriteConsoleInputA
0569 stub WriteConsoleInputVDMA
0570 stub WriteConsoleInputVDMW
0571 stub WriteConsoleInputW
0572 stub WriteConsoleOutputA
0573 stub WriteConsoleOutputAttribute
0574 stub WriteConsoleOutputCharacterA
0575 stub WriteConsoleOutputCharacterW
0576 stub WriteConsoleOutputW
0577 stub WriteConsoleW
0578    stdcall WriteFile(long ptr long ptr ptr) WriteFile
0579 stub WriteFileEx
0580 stub WritePrivateProfileSectionA
0581 stub WritePrivateProfileSectionW
0582 stdcall WritePrivateProfileStringA(ptr ptr ptr ptr)	WritePrivateProfileString
0583 stub WritePrivateProfileStringW
0584 stub WriteProcessMemory
0585 stub WriteProfileSectionA
0586 stub WriteProfileSectionW
0587 stdcall WriteProfileStringA(ptr ptr ptr)	WriteProfileString
0588 stub WriteProfileStringW
0589 stub WriteTapemark
0590 stub _hread
0591 stub _hwrite
0592 stdcall _lclose(long) _lclose
0593 stdcall _lcreat(ptr long) _lcreat
0594 stub _llseek
0595 stdcall _lopen(ptr long) _lopen
0596 stub _lread
0597 stub _lwrite
0598 stdcall lstrcat(ptr ptr) lstrcat32A
0599 stdcall lstrcatA(ptr ptr) lstrcat32A
0600 stdcall lstrcatW(ptr ptr) lstrcat32W
0601 stdcall lstrcmp(ptr ptr) lstrcmp32A
0602 stdcall lstrcmpA(ptr ptr) lstrcmp32A
0603 stdcall lstrcmpW(ptr ptr) lstrcmp32W
0604 stdcall lstrcmpi(ptr ptr) lstrcmpi32A
0605 stdcall lstrcmpiA(ptr ptr) lstrcmpi32A
0606 stdcall lstrcmpiW(ptr ptr) lstrcmpi32W
0607 stdcall lstrcpy(ptr ptr) lstrcpy32A
0608 stdcall lstrcpyA(ptr ptr) lstrcpy32A
0609 stdcall lstrcpyW(ptr ptr) lstrcpy32W
0610 stdcall lstrcpyn(ptr ptr long) lstrcpyn32A
0611 stdcall lstrcpynA(ptr ptr long) lstrcpyn32A
0612 stdcall lstrcpynW(ptr ptr long) lstrcpyn32W
0613 stdcall lstrlen(ptr) lstrlen32A
0614 stdcall lstrlenA(ptr) lstrlen32A
0615 stdcall lstrlenW(ptr) lstrlen32W
#late additions
0616 stub GetPrivateProfileSectionNamesA
0617 stub GetPrivateProfileSectionNamesW
0618 stub GetPrivateProfileStructA
0619 stub GetPrivateProfileStructW
0620 stub GetProcessVersion
0621    stdcall GetSystemPowerStatus(ptr) GetSystemPowerStatus
0622 stub GetSystemTimeAsFileTime
0623 stub HeapCreateTagsW
0624 stub HeapExtend
0625 stub HeapQueryTagW
0626 stub HeapSummary
0627 stub HeapUsage
0628 stub IsDebuggerPresent
0629 stub PostQueuedCompletionStatus
0630    stdcall SetSystemPowerState(long long) SetSystemPowerState
0631 stub WritePrivateProfileStructA
0632 stub WritePrivateProfileStructW
0633 stub MakeCriticalSectionGlobal
