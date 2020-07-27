from SimilarityCalculatorStrategy import SimilarityCalculatorStrategy

CLOSE = 'close'
VOL = 'volume'
OPEN = 'open'
class Alice:
    companies = {}

    similarity_calculator_strategy = SimilarityCalculatorStrategy()

    def add_company(self, company_name, historical):
        self.companies.update({company_name: historical})

    def get_company(self, company_name):
        return self.companies.get(company_name)

    # TODO MOVE DRAWING STUFF HERE

    def compare(self, company_x_name, company_y_name, criteria=OPEN, strategy='cosine'):
        company_x = self.get_company(company_x_name)
        company_y = self.get_company(company_y_name)

        # TODO check companies exist in the dict

        similarity_calculator = self.similarity_calculator_strategy.build_similarity_calculator(strategy)

        # Get only the criteria to be used to compare stocks
        company_x_criteria = company_x[criteria]
        company_y_criteria = company_y[criteria]

        return similarity_calculator.calculate_similarity(company_x_criteria.to_numpy(), company_y_criteria.to_numpy())
