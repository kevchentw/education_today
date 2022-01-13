export interface IAuthor {
  AuthorId: number;
  Rank: number;
  NormalizedName: string;
  DisplayName: number;
  LastKnownAffiliationId?: number;
  PaperCount: number;
  PaperFamilyCount: number;
  CitationCount: number;
  CreatedDate?: Date;
}

export interface IMostCitedPapers {
  PaperId: number;
  Rank: number;
  Doi: string;
  DocType: string;
  PaperTitle: string;
  OriginalTitle: string;
  BookTitle: string;
  Year?: number;
  Date?: Date;
  OnlineDate?: Date;
  Publisher: string;
  JournalId?: number;
  ConferenceSeriesId?: number;
  ConferenceInstanceId?: number;
  Volume: string;
  Issue: string;
  FirstPage: string;
  LastPage: string;
  ReferenceCount: number;
  CitationCount: number;
  EstimatedCitation: number;
  OriginalVenue: string;
  FamilyId: number;
  FamilyRank: number;
  DocSubTypes: string;
  CreatedDate?: Date;
  CitedByCount: number;
}

export interface IAPIMostCitedPaperResponse {
  author: IAuthor;
  results: IMostCitedPapers[];
}
