

export default function validatePermissionsOLD(entity: string, action: string, permissions: string[]): boolean {

    return permissions.includes(`${entity}:${action}`)
}

export const validatePermissions = (entity: string, action: string): any => {
    const toast = useToast();
    const authUserStorage = useAuthUserStorage();
    const permissions = authUserStorage.value.union_permissions_all;


    for (const permission of permissions) {
        if (permission.codename === action + '_' + entity) {
            toast.add({ title: permission.name_es });
            return true; 
        }
    }
    toast.add({ title: 'No tiene permisos para realizar esta acción' });
    return false; 
};
