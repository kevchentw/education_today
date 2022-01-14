import React, { useState } from "react";
import axios from "axios";
import { IAPIMostCitedPaperResponse } from "../types/MostCitedPapers";
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

export default function MostCitedPapers() {
  const [data, setData] = useState<IAPIMostCitedPaperResponse>();
  const [limit, setLimit] = useState(10);
  const [authorId, setAuthorId] = useState(2096520082);
  const [loading, setLoading] = useState(false);

  async function fetchData() {
    try {
      setLoading(true);
      const response = await axios.get("/api/most-cited-papers", {
        params: { limit, authorId },
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
            <FormLabel>Author Id</FormLabel>
            <Input
              value={authorId}
              type="number"
              onChange={(e) => setAuthorId(parseInt(e.target.value))}
            />
          </FormControl>
          <Button colorScheme="blue" onClick={fetchData}>
            Search
          </Button>
        </Stack>
      </Box>
      <Text m={4}>Author: {data?.author.DisplayName}</Text>
      <Table>
        <Thead>
          <Tr>
            <Th>Paper Id</Th>
            <Th>Paper Title</Th>
            <Th>Cited Count</Th>
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
                <Td>{x.PaperId}</Td>
                <Td>{x.OriginalTitle}</Td>
                <Td>{x.CitedByCount}</Td>
              </Tr>
            ))}
          </Tbody>
        )}
      </Table>
    </div>
  );
}
