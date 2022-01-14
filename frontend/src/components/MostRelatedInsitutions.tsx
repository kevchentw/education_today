import React, { useState } from "react";
import axios from "axios";
import { IAPIMostRelatedInsitutionResponse } from "../types/MostRelatedInsitutions";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Button,
  Input,
  FormLabel,
  FormControl,
  Box,
  Stack,
  Text,
  Spinner,
} from "@chakra-ui/react";

export default function MostRelatedInsitutions() {
  const [data, setData] = useState<IAPIMostRelatedInsitutionResponse>();
  const [limit, setLimit] = useState(10);
  const [loading, setLoading] = useState(false);
  const [affiliationId, setAffiliationId] = useState(148366613);

  async function fetchData() {
    try {
      setLoading(true);
      const response = await axios.get("/api/most-related-insitutions", {
        params: { limit, affiliationId },
      });
      setData(response.data);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  }

  return (
    <div>
      <Box w="250px">
        <Stack spacing={3}>
          <FormControl>
            <FormLabel>Limit</FormLabel>
            <Input
              value={limit}
              type="number"
              onChange={(e) => setLimit(parseInt(e.target.value))}
            />
          </FormControl>
          <FormControl>
            <FormLabel>Affiliation Id</FormLabel>
            <Input
              value={affiliationId}
              type="number"
              onChange={(e) => setAffiliationId(parseInt(e.target.value))}
            />
          </FormControl>
          <Button colorScheme="blue" onClick={fetchData}>
            Search
          </Button>
        </Stack>
      </Box>
      <Text>Affiliation: {data?.affiliation.DisplayName}</Text>
      <Table>
        <Thead>
          <Tr>
            <Th>Affiliation Id</Th>
            <Th>Display Name</Th>
            <Th>Related Count</Th>
          </Tr>
        </Thead>
        {loading ? (
          <Box w="100%" p={4}>
            <Spinner />
          </Box>
        ) : (
          <Tbody>
            {data?.results.map((x) => (
              <Tr>
                <Td>{x.AffiliationId}</Td>
                <Td>{x.DisplayName}</Td>
                <Td>{x.RelatedCount}</Td>
              </Tr>
            ))}
          </Tbody>
        )}
      </Table>
    </div>
  );
}
