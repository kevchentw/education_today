export interface IAffiliation {
  AffiliationId: number;
  Rank: number;
  NormalizedName: string;
  DisplayName: string;
  GridId: string;
  OfficialPage: string;
  WikiPage: string;
  PaperCount: number;
  PaperFamilyCount: number;
  CitationCount: number;
  Iso3166Code: string;
  Latitude?: number;
  Longitude?: number;
  CreatedDate?: number;
}

export interface IMostRelatedInsitutions {
  AffiliationId: number;
  Rank: number;
  NormalizedName: string;
  DisplayName: string;
  GridId: string;
  OfficialPage: string;
  WikiPage: string;
  PaperCount: number;
  PaperFamilyCount: number;
  CitationCount: number;
  Iso3166Code: string;
  Latitude?: number;
  Longitude?: number;
  CreatedDate?: Date;
  RelatedCount: number;
}

export interface IAPIMostRelatedInsitutionResponse {
  affiliation: IAffiliation;
  results: IMostRelatedInsitutions[];
}
