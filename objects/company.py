class Company:
	"""Represents a physical retailer chain."""

    def __init__(self, company_name):

        self.name = company_name
        self.min_zip_cover = set()

    def set_min_zip_cover(self, a_min_zip_cover):
    	"""Sets min zip code cover for a company"""

        self.min_zip_cover = a_min_zip_cover