# Coronavirus Disease (COVID-19) US Testing Data | The COVID Tracking Project

The source code outlining how this product gathers, transforms, revises and publishes its datasets is available at [https://github.com/rearc-data/covid-19-testing-data](https://github.com/rearc-data/covid-19-testing-data).

## Main Overview
The COVID Tracking Project collects information from 50 US states, the District of Columbia, and 5 other US territories to provide the most comprehensive testing data for the novel coronavirus, SARS-CoV-2. The dataset includes positive and negative results, pending tests, and total people tested for each state or district currently reporting that data.

The data is collected from state/district/territory public health authorities or, occasionally, from trusted news reporting, official press conferences, or (very occasionally) tweets or Facebook updates from state public health authorities or governors.

If you are interested in exploring this product on GitHub, please click [here](https://github.com/rearc-data/covid-19-testing-data).

#### Data Sources
All datasets are in both CSV and JSON format:
- States current testing data (`states_current`)
- States historical testing data (`states_daily`)
- States specific resources (`states_info`)
- US current testing data (`us_current`)
- US historical testing data (`us_daily`)
- State website screenshots (`states_screenshots`)

For information about the specific columns in each dataset visit the [Data API Documentation](https://covidtracking.com/api) page on The COVID Tracking Project's website.

### Changelog
#### 2020-6-4
- The `countries`, `cdc_daily`, `urls` and `press` datasets have been removed from this product, as these data sources are no longer publicly accessible through the COVID Tracking Project's API.

## More Information
- [Source | The COVID Tracking Project Hompage](https://covidtracking.com/)  
- [Schema Definitions | Data API Documentation](https://covidtracking.com/api)
- [Sample Data](https://covidtracking.com/data/)   
- [Terms of Use](https://covidtracking.com/license)
- Frequency: Every 2 hours
- Formats: CSV, JSON

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc-data/covid-19-testing-data/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about the source data, please contact [The COVID Tracking Project](https://covidtracking.com/contact).
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
