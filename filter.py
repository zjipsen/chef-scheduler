class Filter: 

    # Public Methods ###################################################################

    """ALLOWS COOKING 2 DAYS IN A ROW IF NECESSARY"""
    # def yesterday(self, yesterday_chefs, w_chefs):
    # 	def weight_cooked_yesterday(w_chef, y_chefs):
    # 		if (w_chef.chef.name in y_chefs):
    # 			w_chef.weight = w_chef.weight - 1
    # 		return w_chef
    		
    # 	if len(yesterday_chefs) > 0:
    # 		w_chefs = [weight_cooked_yesterday(w_chef, yesterday_chefs) for w_chef in w_chefs]
    # 		w_chefs.sort(reverse=True, key=lambda wc: wc.weight)
    # 		return w_chefs
    # 	return w_chefs

    """DOES NOT ALLOW COOKING 2 DAYS IN A ROW"""
    def yesterday(self, yesterday_chefs, w_chefs):
    	if len(yesterday_chefs) > 0:
    		return self._filter(lambda w_chef: w_chef.chef.name not in yesterday_chefs, w_chefs)
    	return w_chefs

    """ALLOWS ROOMMATES TO COOK ON THE SAME DAY IF NECESSARY"""
    # def roommates(self, main, roommates, w_chefs):
    # 	def weight_roommates(main, roommates, w_chef):
    # 		if (w_chef.chef.name in roommates[main.name]):
    # 			w_chef.weight = w_chef.weight - 3
    # 		return w_chef
    		
    # 	if main is not None:
    # 		w_chefs = [weight_roommates(main, roommates, w_chef) for w_chef in w_chefs]
    # 		w_chefs.sort(reverse=True, key=lambda wc: wc.weight)
    # 		return w_chefs
    # 	return w_chefs

    """DOES NOT ALLOW ROOMMATES TO COOK ON THE SAME DAY"""
    def roommates(self, main, roommates, w_chefs):
    	if main and roommates:
    		return self._filter(lambda w_chef: w_chef.chef.name not in roommates[main.name], w_chefs)
    	return w_chefs

    def same_person(self, main, w_chefs):
    	if main:
    		return self._filter(lambda w_chef: w_chef.chef.name != main.name, w_chefs)
    	return w_chefs

    # Private Methods ###################################################################

    def _filter(self, func, input):
    	return list(filter(func, input))

    def _map(self, func, input):
    	return list(map(func, input))
