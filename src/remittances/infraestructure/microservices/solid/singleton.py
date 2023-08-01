class SolidOperationSingleton:
    """
    Solid singleton to be init in the app.py of the microservice, with instance property we can re use
    the client without create multiple instances.
    """

    class __SolidSingleton:
        def __init__(self, base_url, service_key):

            self.base_url = base_url
            self.service_key = service_key

    instance = None

    def __init__(self, base_url, service_key):
        if not SolidOperationSingleton.instance:
            SolidOperationSingleton.instance = SolidOperationSingleton.__SolidSingleton(
                base_url=base_url,
                service_key=service_key
            )
                                                                    
        else:
            SolidOperationSingleton.instance.base_url = base_url
            SolidOperationSingleton.instance.service_key = service_key

    def __getattr__(self, name):
        return self.instance.__getattribute__(name)
