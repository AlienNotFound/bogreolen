import vercel_blob

class ImageService:   
    @staticmethod 
    def upload_a_blob(file):
        if file:
            if ImageService.file_validation(file):
                result = vercel_blob.put(file.filename,
                                        file.read(), {
                                            "addRandomSuffix": "true",
                                        })

                return 'Success', result['url']
            else:
                return 'Error', 'Invalid filetype'
        else:
            return 'Error', None
    
    @staticmethod
    def delete_blob(file):
        if file:
            result = vercel_blob.delete(file)
            return 'Success', 'File deleted'
        else:
            return 'Error', None
        
    @staticmethod
    def file_validation(file):
        expected_extention = ['png', 'jpg', 'jpeg']
        file_extention = file.filename.split('.', 1)[-1].lower()

        return file_extention in expected_extention