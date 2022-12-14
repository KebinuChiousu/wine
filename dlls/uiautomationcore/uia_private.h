/*
 * Copyright 2022 Connor McAdams for CodeWeavers
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#define COBJMACROS

#include "uiautomation.h"
#include "uia_classes.h"

extern HMODULE huia_module DECLSPEC_HIDDEN;

enum uia_prop_type {
    PROP_TYPE_UNKNOWN,
    PROP_TYPE_ELEM_PROP,
    PROP_TYPE_SPECIAL,
};

struct uia_node {
    IWineUiaNode IWineUiaNode_iface;
    LONG ref;

    IWineUiaProvider *prov;
    DWORD git_cookie;

    HWND hwnd;
    BOOL nested_node;
};

static inline struct uia_node *impl_from_IWineUiaNode(IWineUiaNode *iface)
{
    return CONTAINING_RECORD(iface, struct uia_node, IWineUiaNode_iface);
}

/* uia_ids.c */
const struct uia_prop_info *uia_prop_info_from_id(PROPERTYID prop_id) DECLSPEC_HIDDEN;

/* uia_provider.c */
void uia_stop_provider_thread(void) DECLSPEC_HIDDEN;
