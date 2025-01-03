# CHEESE similarity search with multiple similarity measures and against various databases

CHEESE is a chemical embeddings search engine based on approximate nearest neighbors. It supports multiple similarity measures and can search against various databases, including ENAMINE REAL, ZINC, and others. Among the similarity measures, CHEESE supports the classical Morgan fingerprints as well as 3D shape and electrostatics similarities. The search engine is available online. This model from the Ersilia Model Hub is intended to be used a sampler for the CHEESE search engine, where the user can input a compound and get a list of similar compounds as output. The database used for the search, the similarity measure, and the filters are randomly chosen for each query.

## Identifiers

* EOS model ID: `eos9uqy`
* Slug: `cheese-sampler`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Similarity`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: A list of up to 100 similar compounds to the input compound.

## References

* [Publication](https://chemrxiv.org/engage/chemrxiv/article-details/67250915f9980725cfcd1f6f)
* [Source Code](https://cheese.deepmedchem.com/)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9uqy)

## Citation

If you use this model, please cite the [original authors](https://chemrxiv.org/engage/chemrxiv/article-details/67250915f9980725cfcd1f6f) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0-or-later license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!